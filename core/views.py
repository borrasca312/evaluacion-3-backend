from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empresa, Servicio, Profesional, OrdenServicio
from .forms import EmpresaForm, ServicioForm, ProfesionalForm, OrdenServicioForm

"""
Vistas genéricas (Class-Based Views) para las operaciones CRUD.

Características:
  - ListViews con búsqueda por query (parámetro GET 'q').
  - LoginRequiredMixin en Create/Update/Delete (solo usuarios autenticados).
  - DetailViews para ver detalles de cada entidad.
  - Búsqueda case-insensitive usando Q() con icontains.
"""


class EmpresaListView(ListView):
    """
    Listado de empresas con búsqueda.
    
    Búsqueda: parámetro GET 'q' busca en RUT, razón social y email.
    Ejemplo: /empresas/?q=PYME
    """
    model = Empresa
    template_name = 'core/empresa_list.html'
    
    def get_queryset(self):
        """Aplica filtro de búsqueda si existe el parámetro 'q' en la URL."""
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(razon_social__icontains=q) | Q(rut__icontains=q) | Q(email__icontains=q)
            )
        return qs


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'core/empresa_detail.html'


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    """
    Crear empresa. Protegida con LoginRequiredMixin.
    Solo usuarios autenticados pueden acceder. Redirige a login si no está autenticado.
    """
    model = Empresa
    form_class = EmpresaForm
    template_name = 'core/empresa_form.html'
    success_url = reverse_lazy('empresa_list')


class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'core/empresa_form.html'
    success_url = reverse_lazy('empresa_list')


class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'core/empresa_confirm_delete.html'
    success_url = reverse_lazy('empresa_list')


# Servicio views
class ServicioListView(ListView):
    model = Servicio
    template_name = 'core/servicio_list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(nombre__icontains=q) | Q(descripcion__icontains=q) | Q(categoria__icontains=q)
            )
        return qs


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'core/servicio_detail.html'


class ServicioCreateView(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'core/servicio_form.html'
    success_url = reverse_lazy('servicio_list')


class ServicioUpdateView(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'core/servicio_form.html'
    success_url = reverse_lazy('servicio_list')


class ServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = Servicio
    template_name = 'core/servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')


# Profesional views
class ProfesionalListView(ListView):
    model = Profesional
    template_name = 'core/profesional_list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(nombres__icontains=q) | Q(apellidos__icontains=q) | Q(run__icontains=q) | Q(email__icontains=q)
            )
        return qs


class ProfesionalDetailView(DetailView):
    model = Profesional
    template_name = 'core/profesional_detail.html'


class ProfesionalCreateView(LoginRequiredMixin, CreateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'core/profesional_form.html'
    success_url = reverse_lazy('profesional_list')


class ProfesionalUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'core/profesional_form.html'
    success_url = reverse_lazy('profesional_list')


class ProfesionalDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesional
    template_name = 'core/profesional_confirm_delete.html'
    success_url = reverse_lazy('profesional_list')


# OrdenServicio views
class OrdenServicioListView(ListView):
    """
    Listado de órdenes de servicio con búsqueda y filtros avanzados.
    
    Parámetros GET:
        - 'q': Búsqueda general en empresa, descripción y profesional asignado.
        - 'estado': Filtrar por estado (nueva, en_ejecucion, finalizada, cancelada).
        - 'prioridad': Filtrar por prioridad (baja, media, alta).
        - 'empresa': Búsqueda por nombre o RUT de empresa.
    
    Ejemplo: /ordenes/?q=diagnóstico&estado=nueva&prioridad=alta
    """
    model = OrdenServicio
    template_name = 'core/orden_list.html'

    def get_queryset(self):
        """Aplica filtros múltiples según parámetros GET."""
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        estado = self.request.GET.get('estado', '').strip()
        prioridad = self.request.GET.get('prioridad', '').strip()
        empresa = self.request.GET.get('empresa', '').strip()

        # Búsqueda general (Q con OR)
        if q:
            qs = qs.filter(
                Q(empresa__razon_social__icontains=q)
                | Q(descripcion_requerimiento__icontains=q)
                | Q(profesional_asignado__nombres__icontains=q)
                | Q(profesional_asignado__apellidos__icontains=q)
            )
        
        # Filtros específicos
        if estado:
            qs = qs.filter(estado=estado)
        if prioridad:
            qs = qs.filter(prioridad=prioridad)
        if empresa:
            qs = qs.filter(Q(empresa__razon_social__icontains=empresa) | Q(empresa__rut__icontains=empresa))

        return qs


class OrdenServicioDetailView(DetailView):
    model = OrdenServicio
    template_name = 'core/orden_detail.html'


class OrdenServicioCreateView(LoginRequiredMixin, CreateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = 'core/orden_form.html'
    success_url = reverse_lazy('orden_list')


class OrdenServicioUpdateView(LoginRequiredMixin, UpdateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = 'core/orden_form.html'
    success_url = reverse_lazy('orden_list')


class OrdenServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = OrdenServicio
    template_name = 'core/orden_confirm_delete.html'
    success_url = reverse_lazy('orden_list')
