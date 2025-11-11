from django import forms
from .models import Empresa, Servicio, Profesional, OrdenServicio


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['rut', 'razon_social', 'giro', 'telefono', 'email', 'direccion', 'comuna']


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'categoria', 'duracion_estimada_horas', 'activo']


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['run', 'nombres', 'apellidos', 'especialidad', 'email']


class OrdenServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        fields = ['empresa', 'estado', 'prioridad', 'descripcion_requerimiento', 'servicios_seleccionados', 'profesional_asignado']
