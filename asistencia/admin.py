from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Estudiante, Asistencia

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    list_filter = ('nombre',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('get_estudiante', 'get_fecha', 'get_hora')
    search_fields = ('estudiante__nombre',)
    ordering = ('-fecha', 'hora')
    list_filter = ('fecha', 'hora')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('estudiante')

    def get_estudiante(self, obj):
        return obj.estudiante.nombre if obj.estudiante else _('Desconocido')
    get_estudiante.admin_order_field = 'estudiante__nombre'
    get_estudiante.short_description = _('Estudiante')

    def get_fecha(self, obj):
        return obj.fecha.strftime('%d/%m/%Y')
    get_fecha.admin_order_field = 'fecha'
    get_fecha.short_description = _('Fecha')

    def get_hora(self, obj):
        return obj.hora.strftime('%H:%M:%S')
    get_hora.admin_order_field = 'hora'
    get_hora.short_description = _('Hora')

# Esto permite que el administrador de Django muestre los campos de fecha y hora en un formato más legible.
# Esto es necesario para que el administrador de Django pueda mostrar los modelos de asistencia y estudiante.
# También se pueden agregar más configuraciones según sea necesario, como acciones personalizadas, campos adicionales, etc.

