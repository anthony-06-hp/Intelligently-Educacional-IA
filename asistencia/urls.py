from django.urls import path
from .views import reconocer_asistencia, register_view

urlpatterns = [
    path('reconocer_asistencia/', reconocer_asistencia, name='reconocer_asistencia'),
    path('register', register_view , name='register_view'),
]