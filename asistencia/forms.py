from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Estudiante

User = get_user_model()

class RegistroEstudianteForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=150, required=True)
    apellido = forms.CharField(max_length=150, required=True)
    cedula = forms.CharField(max_length=20, required=True)
    curso = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellido', 'cedula', 'curso']

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Estudiante.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError("La cédula ya está registrada.")
        return cedula

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Estudiante.objects.create(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                cedula=self.cleaned_data['cedula'],
                curso=self.cleaned_data['curso'],
            )
        return user
