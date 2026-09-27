from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_redirect_view
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_redirect_view, name='home'),
    path('core/', include('core.urls')),
    path('accounts/', include('accounts.urls')),  # Esto es fundamental
    path('recursos/', include('recursos.urls')),
    path('reportes/', include('reportes.urls')),
    path('videollamadas/', include('videollamadas.urls')),
    path('calendario/', include('calendario.urls')),
    path('asistencia/', include('asistencia.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
