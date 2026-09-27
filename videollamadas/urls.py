from django.urls import path
from . import views
app_name = 'videollamadas'
urlpatterns = [
    path('', views.index, name='videollamadas_home'),
]
