from django.db import models
from datetime import date
from django.db import models
from django.conf import settings

class Estudiante(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    hora = models.TimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'fecha')

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.fecha}"   