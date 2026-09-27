from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from deepface import DeepFace
import numpy as np
import joblib
import cv2
from PIL import Image
from datetime import date
from .models import Estudiante, Asistencia
from .forms import RegistroEstudianteForm  # Asegúrate de que este formulario esté definido en forms.py
import os
import subprocess
import sys
@csrf_exempt
def reconocer_asistencia(request):
    if request.method == 'GET':
        return render(request, 'asistencia.html')  # asegúrate de que existe el archivo en templates/asistencia.html

    elif request.method == 'POST':
        image_file = request.FILES.get('imagen')
        if not image_file:
            return JsonResponse({'mensaje': 'No se recibió imagen'})

        image = Image.open(image_file).convert('RGB')
        frame = np.array(image)

        try:
            results = DeepFace.represent(
                frame, model_name='VGG-Face',
                enforce_detection=False,
                detector_backend='opencv'
            )

            if not results or 'embedding' not in results[0]:
                return JsonResponse({'mensaje': 'No se detectó un rostro válido en la imagen'})

            embedding = results[0]['embedding']

            clf = joblib.load('knn_vggface_classifier.joblib')
            scaler = joblib.load('scaler.joblib')
            embedding_scaled = scaler.transform([embedding])
            probs = clf.predict_proba(embedding_scaled)[0]
            pred = clf.classes_[np.argmax(probs)]
            confidence = np.max(probs)

            if confidence > 0.6:
                estudiante = Estudiante.objects.get(nombre=pred)
                asistencia, created = Asistencia.objects.get_or_create(estudiante=estudiante, fecha=date.today())
                mensaje = f"Asistencia registrada para {pred}" if created else f"Asistencia ya registrada para {pred}"
                return JsonResponse({'mensaje': mensaje})
            else:
                return JsonResponse({'mensaje': 'Rostro no reconocido con suficiente confianza'})

        except Exception as e:
            return JsonResponse({'mensaje': 'Error en reconocimiento: ' + str(e)})


    # Si el método no es GET ni POST
    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import RegistroEstudianteForm

def register_view(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            user = form.save()
            estudiante = Estudiante.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                cedula=form.cleaned_data['cedula'],
                curso=form.cleaned_data['curso']
            )

            # Verificar si ya tiene fotos (dataset/personaX)
            persona_dir = os.path.join('dataset', f"{estudiante.nombre.replace(' ', '_')}")
            if not os.path.exists(persona_dir) or len(os.listdir(persona_dir)) == 0:
                # Captura de rostro (solo la primera vez)
                script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'capturar.py'))
                subprocess.Popen([sys.executable, script_path, estudiante.nombre.replace(" ", "_")])

            return redirect('asistencia')  # Mostrar interfaz de asistencia
    else:
        form = RegistroEstudianteForm()
    return render(request, 'asistencia/register.html', {'form': form})
