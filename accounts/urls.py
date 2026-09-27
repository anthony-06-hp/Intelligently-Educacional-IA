from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_page, name='login_page'),  # Para GET y mostrar formulario
    path('login/api/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('ajax/login/', views.ajax_login, name='ajax_login'),  # Para funcionalidad AJAX opcional
    path('api/dashboard-stats/', views.api_dashboard_stats, name='api_dashboard_stats'),
    path('api/courses/', views.api_courses, name='api_courses'),
    path('perfil/', views.profile_view, name='profile'),
    path('eliminar-cuenta/', views.delete_user_view, name='delete_account'),
    path('captura-rostro/', views.captura_rostro, name='captura_rostro'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/<int:curso_id>/inscribir/', views.inscribir_estudiantes, name='inscribir_estudiantes'),
    path('listar-cursos/', views.listar_cursos, name='listar_cursos'),

]    
