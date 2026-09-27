from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    institution = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    interests = models.CharField(max_length=255, blank=True, null=True)

    # Perfil
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    avatar = models.CharField(max_length=10, blank=True, null=True)  # Guardamos emoji o código avatar

    ROLE_CHOICES = [
            ('estudiante', 'Estudiante'),
            ('docente', 'Docente'),
            ('administrador', 'Administrador'),
        ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='estudiante')
    face_folder = models.CharField(max_length=100, blank=True, null=True)  # <- NUEVO CAMPO
    def __str__(self):
            return f'{self.username} ({self.role})'
    
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    asignaturas = models.ManyToManyField(Asignatura)
    docentes = models.ManyToManyField('CustomUser', limit_choices_to={'role': 'docente'})
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    estudiante = models.ForeignKey('CustomUser', on_delete=models.CASCADE, limit_choices_to={'role': 'estudiante'})
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  # Para evitar duplicados

    def __str__(self):
        return f'{self.estudiante.full_name} inscrito en {self.curso.nombre}'
