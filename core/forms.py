from django import forms
from .models import Empresa, Servicio, Profesional, OrdenServicio

"""
Formularios ModelForm para las operaciones CRUD.

Los formularios heredan campos del modelo automáticamente.
Django valida campos con unique=True, EmailField, y otros automáticamente.
"""


class EmpresaForm(forms.ModelForm):
    """Formulario para crear/editar empresas."""
    class Meta:
        model = Empresa
        fields = ['rut', 'razon_social', 'giro', 'telefono', 'email', 'direccion', 'comuna']


class ServicioForm(forms.ModelForm):
    """Formulario para crear/editar servicios."""
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'categoria', 'duracion_estimada_horas', 'activo']


class ProfesionalForm(forms.ModelForm):
    """Formulario para crear/editar profesionales."""
    class Meta:
        model = Profesional
        fields = ['run', 'nombres', 'apellidos', 'especialidad', 'email']


class OrdenServicioForm(forms.ModelForm):
    """
    Formulario para crear/editar órdenes de servicio.
    Incluye relaciones ManyToMany (servicios_seleccionados) y ForeignKey (empresa, profesional).
    """
    class Meta:
        model = OrdenServicio
        fields = ['empresa', 'estado', 'prioridad', 'descripcion_requerimiento', 'servicios_seleccionados', 'profesional_asignado']
