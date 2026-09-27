from django.urls import path
from . import views

app_name = 'recursos'

urlpatterns = [
    path('', views.index, name='recursos_home'),
]
