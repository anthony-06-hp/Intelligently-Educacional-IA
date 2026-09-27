from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model,get_backends
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
import json
from .forms import ProfileUpdateForm

User = get_user_model()

def login_page(request):
    # Vista que solo muestra el formulario HTML para login
    return render(request, 'accounts/login.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Buscar usuario por email para obtener username (si usas username para auth)
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None

        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')  # Cambia a la URL que quieres después de login
            else:
                messages.error(request, 'Contraseña incorrecta.')
        else:
            messages.error(request, 'No existe un usuario con ese email.')

        # En caso de error vuelve a renderizar el formulario con mensajes
        return render(request, 'accounts/login.html')

    else:
        # GET, solo mostrar el formulario
        return render(request, 'accounts/login.html')
from django.contrib.auth import login  # Asegúrate de tener esto importado

from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        # Recogida de datos
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        role = request.POST.get('role')
        mobile = request.POST.get('mobile')
        institution = request.POST.get('institution')
        degree = request.POST.get('degree')
        major = request.POST.get('major')
        graduation_year = request.POST.get('graduationYear') or None
        gpa = request.POST.get('gpa') or None
        date_of_birth = request.POST.get('dateOfBirth') or None
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')
        interests = request.POST.get('interests')
        avatar = request.POST.get('avatar')
        profile_picture = request.FILES.get('profilePicture')

        # Validaciones
        if not full_name or not email or not password or not confirm_password:
            messages.error(request, 'Por favor completa todos los campos obligatorios.')
            return render(request, 'accounts/register.html')

        if len(password) < 2:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return render(request, 'accounts/register.html')

        if '@' not in email:
            messages.error(request, 'Por favor ingresa un email válido.')
            return render(request, 'accounts/register.html')

        if not role or role not in ['estudiante', 'docente', 'administrador']:
            messages.error(request, 'Por favor selecciona un rol válido.')
            return render(request, 'accounts/register.html')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está en uso.')
            return render(request, 'accounts/register.html')

        # Crear usuario
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            full_name=full_name,
            mobile=mobile,
            institution=institution,
            degree=degree,
            major=major,
            graduation_year=graduation_year,
            gpa=gpa,
            date_of_birth=date_of_birth,
            gender=gender,
            country=country,
            city=city,
            interests=interests,
            avatar=avatar,
            profile_picture=profile_picture,
            role=role,
        )

        # Carpeta del rostro
        user.face_folder = f'persona{user.id}'
        user.save()

        # Login
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)

        # Guardar ID
        request.session['nuevo_usuario_id'] = user.id

        # Mostrar alerta y redirigir
        return HttpResponse("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro exitoso</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .modal {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 400px;
            width: 90%;
        }

        .modal h2 {
            color: #333;
            margin-bottom: 15px;
        }

        .modal p {
            color: #555;
            margin-bottom: 25px;
        }

        .btn {
            background-color: #007bff;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }

        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="modal">
        <h2>¡Registro completado!</h2>
        <p>Para completar el proceso, se capturarán imágenes de tu rostro para el reconocimiento facial.</p>
        <button class="btn" onclick="window.location.href='/accounts/captura-rostro/'">Continuar</button>
    </div>
</body>
</html>
""")


    return render(request, 'accounts/register.html')


@login_required
def dashboard_view(request):
    user_data = {
        'full_name': request.user.full_name,
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
    }

    dashboard_data = {
        'courses': [
            {
                'id': 1,
                'title': 'CURSO',
                'created_date': '9 DE MAYO 24:20',
                'subject': 'VERSIÓN',
                'description': 'Fundamentos de la física básica',
                'version': 1
            },
            {
                'id': 2,
                'title': 'CURSO',
                'created_date': '9 DE MAYO 24:20',
                'subject': 'VERSIÓN',
                'description': 'LA MANERA CORRECTA DE LAS TAREAS DOMICILIARIAS',
                'version': 1
            }
        ],
        'assignments': [
            {
                'id': 1,
                'subject': 'Física',
                'icon': '⚗️',
                'icon_class': 'physics-icon',
                'description': 'La Física es la ciencia que estudia los fenómenos naturales, relacionados con la materia, la energía y el movimiento...'
            },
            {
                'id': 2,
                'subject': 'Lengua y Literatura',
                'icon': '📚',
                'icon_class': 'literature-icon',
                'description': 'La asignatura de Lengua y Literatura tiene como propósito que los estudiantes desarrollen las destrezas necesarias...'
            }
        ],
        'stats': {
            'learning_average': 73,
            'total_students': 156,
            'active_courses': 12,
            'completed_assignments': 48
        }
    }

    context = {
        'user_data': user_data,
        'dashboard_data': dashboard_data,
        'page_title': 'Dashboard',
        'user': request.user,
        'stats': {
            'total_users': User.objects.count(),
            'active_projects': 89,
            'completed_tasks': 456,
            'revenue': 12345,
        }
    }

    return render(request, 'accounts/dashboard.html', context)


@csrf_protect
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('accounts:login_page')


@login_required
def api_dashboard_stats(request):
    if request.method == 'GET':
        stats = {
            'learning_average': 73,
            'total_students': 156,
            'active_courses': 12,
            'completed_assignments': 48,
            'recent_activity': [
                {
                    'type': 'course_completed',
                    'message': 'Curso de Física completado',
                    'timestamp': '2024-05-09T14:30:00Z'
                },
                {
                    'type': 'assignment_submitted',
                    'message': 'Tarea de Literatura entregada',
                    'timestamp': '2024-05-09T12:15:00Z'
                }
            ]
        }
        return JsonResponse(stats)
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@login_required
def api_courses(request):
    if request.method == 'GET':
        courses = [
            {
                'id': 1,
                'title': 'Fundamentos de Física',
                'description': 'Curso básico de física',
                'created_date': '2024-05-09',
                'status': 'active'
            },
            {
                'id': 2,
                'title': 'Tareas Domiciliarias',
                'description': 'Métodos efectivos para tareas en casa',
                'created_date': '2024-05-09',
                'status': 'active'
            }
        ]
        return JsonResponse({'courses': courses})
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_data = {
                'id': 3,
                'title': data.get('title'),
                'description': data.get('description'),
                'created_date': '2024-05-09',
                'status': 'active'
            }
            return JsonResponse({'success': True, 'course': course_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_protect
def ajax_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': f'¡Bienvenido {user.get_full_name() or user.username}!',
                    'redirect_url': reverse('accounts:dashboard')
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Usuario o contraseña incorrectos.'
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })

    return JsonResponse({'success': False, 'message': 'Método no permitido.'})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.full_name = request.POST.get('full_name')
        user.mobile = request.POST.get('mobile')
        user.institution = request.POST.get('institution')
        user.degree = request.POST.get('degree')
        user.major = request.POST.get('major')
        user.graduation_year = request.POST.get('graduation_year') or None
        user.gpa = request.POST.get('gpa') or None
        user.date_of_birth = request.POST.get('date_of_birth') or None
        user.gender = request.POST.get('gender')
        user.country = request.POST.get('country')
        user.city = request.POST.get('city')
        user.interests = request.POST.get('interests')

        # Imagen de perfil si fue subida
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']

        user.save()
        messages.success(request, 'Perfil actualizado con éxito.')
        return redirect('accounts:profile')

    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada.')
        return redirect('accounts:login_page')

import os
import sys
import subprocess
from django.conf import settings

@login_required
def captura_rostro(request):
    user_id = request.session.get('nuevo_usuario_id')
    if not user_id:
        messages.error(request, 'No se encontró el usuario.')
        return redirect('accounts:register')

    try:
        user = User.objects.get(id=user_id)
        if not user.face_folder:
            user.face_folder = f"persona{user.id}"
            user.save()

        folder_name = user.face_folder

        # Ruta absoluta al script de captura
        script_path = os.path.join(settings.BASE_DIR, 'accounts', 'scripts', 'captura.py')

        # Ejecutar y esperar a que termine
        subprocess.run([sys.executable, script_path, folder_name])

        # Redirigir al dashboard cuando termina
        return redirect('accounts:dashboard')

    except User.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('accounts:register')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso, CustomUser, Inscripcion
from django.contrib import messages


def es_admin(user):
    return user.is_authenticated and user.role == 'administrador'


@login_required
@user_passes_test(es_admin)
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'inscripciones/listar_cursos.html', {'cursos': cursos})
@login_required
@user_passes_test(es_admin)
def inscribir_estudiantes(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = CustomUser.objects.filter(role='estudiante')

    if request.method == 'POST':
        seleccionados = request.POST.getlist('estudiantes')
        for estudiante_id in seleccionados:
            estudiante = CustomUser.objects.get(id=estudiante_id)
            Inscripcion.objects.get_or_create(estudiante=estudiante, curso=curso)
        messages.success(request, 'Estudiantes inscritos correctamente.')
        return redirect('listar_cursos')

    ya_inscritos = Inscripcion.objects.filter(curso=curso).values_list('estudiante_id', flat=True)
    return render(request, 'inscripciones/inscribir_estudiantes.html', {
        'curso': curso,
        'estudiantes': estudiantes,
        'ya_inscritos': ya_inscritos,
    })


def home_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    return redirect('accounts:login_page')
