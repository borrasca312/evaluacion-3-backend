from django.urls import path
from . import views

urlpatterns = [
    # Empresa
    path('empresas/', views.EmpresaListView.as_view(), name='empresa_list'),
    path('empresas/<int:pk>/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('empresas/crear/', views.EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresas/<int:pk>/editar/', views.EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresas/<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='empresa_delete'),

    # Servicio
    path('servicios/', views.ServicioListView.as_view(), name='servicio_list'),
    path('servicios/<int:pk>/', views.ServicioDetailView.as_view(), name='servicio_detail'),
    path('servicios/crear/', views.ServicioCreateView.as_view(), name='servicio_create'),
    path('servicios/<int:pk>/editar/', views.ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicios/<int:pk>/eliminar/', views.ServicioDeleteView.as_view(), name='servicio_delete'),

    # Profesional
    path('profesionales/', views.ProfesionalListView.as_view(), name='profesional_list'),
    path('profesionales/<int:pk>/', views.ProfesionalDetailView.as_view(), name='profesional_detail'),
    path('profesionales/crear/', views.ProfesionalCreateView.as_view(), name='profesional_create'),
    path('profesionales/<int:pk>/editar/', views.ProfesionalUpdateView.as_view(), name='profesional_update'),
    path('profesionales/<int:pk>/eliminar/', views.ProfesionalDeleteView.as_view(), name='profesional_delete'),

    # OrdenServicio
    path('', views.OrdenServicioListView.as_view(), name='orden_list'),
    path('ordenes/<int:pk>/', views.OrdenServicioDetailView.as_view(), name='orden_detail'),
    path('ordenes/crear/', views.OrdenServicioCreateView.as_view(), name='orden_create'),
    path('ordenes/<int:pk>/editar/', views.OrdenServicioUpdateView.as_view(), name='orden_update'),
    path('ordenes/<int:pk>/eliminar/', views.OrdenServicioDeleteView.as_view(), name='orden_delete'),
]
