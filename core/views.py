from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empresa, Servicio, Profesional, OrdenServicio
from .forms import EmpresaForm, ServicioForm, ProfesionalForm, OrdenServicioForm


class EmpresaListView(ListView):
    model = Empresa
    template_name = 'core/empresa_list.html'


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'core/empresa_detail.html'


class EmpresaCreateView(LoginRequiredMixin, CreateView):
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
    model = OrdenServicio
    template_name = 'core/orden_list.html'


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
