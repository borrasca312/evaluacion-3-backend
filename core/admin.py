from django.contrib import admin
from .models import Empresa, Servicio, Profesional, OrdenServicio


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('rut', 'razon_social', 'giro', 'telefono', 'email', 'comuna')
    search_fields = ('rut', 'razon_social', 'email')
    ordering = ('razon_social',)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'duracion_estimada_horas', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')


@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('run', 'nombres', 'apellidos', 'especialidad', 'email')
    search_fields = ('run', 'nombres', 'apellidos', 'email')


def marcar_en_ejecucion(modeladmin, request, queryset):
    queryset.update(estado='en_ejecucion')
    marcar_en_ejecucion.short_description = 'Marcar seleccionadas como en ejecución'


def marcar_finalizada(modeladmin, request, queryset):
    queryset.update(estado='finalizada')
    marcar_finalizada.short_description = 'Marcar seleccionadas como finalizada'


@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'fecha_creacion', 'estado', 'prioridad', 'profesional_asignado')
    list_filter = ('estado', 'prioridad', 'empresa')
    search_fields = ('empresa__razon_social', 'descripcion_requerimiento')
    ordering = ('-fecha_creacion',)
    readonly_fields = ('fecha_creacion',)
    actions = [marcar_en_ejecucion, marcar_finalizada]
