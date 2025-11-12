"""
Script para inicializar el proyecto después de clonar/descargar desde GitHub
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command
from core.models import Empresa, Servicio, Profesional, OrdenServicio

print("=" * 60)
print("INICIALIZANDO PROYECTO - Sistema de Gestión INACAP")
print("=" * 60)
print()

# 1. Crear superusuario
print("1. Creando usuario administrador...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    print("   ✓ Usuario creado: admin")
    print("   ✓ Contraseña: admin123")
else:
    print("   ℹ Usuario 'admin' ya existe")

print()

# 2. Crear datos de ejemplo
print("2. Creando datos de ejemplo...")

# Empresa
if not Empresa.objects.exists():
    empresa = Empresa.objects.create(
        rut='76.123.456-7',
        razon_social='PYME Ejemplo S.A.',
        giro='Comercio al por menor',
        telefono='+56912345678',
        email='contacto@pymeejemplo.cl',
        direccion='Av. Principal 123',
        comuna='Santiago'
    )
    print(f"   ✓ Empresa: {empresa.razon_social}")
else:
    empresa = Empresa.objects.first()
    print(f"   ℹ Empresa ya existe: {empresa.razon_social}")

# Servicios
if not Servicio.objects.exists():
    servicio1 = Servicio.objects.create(
        nombre='Diagnóstico tecnológico',
        descripcion='Evaluación de infraestructura tecnológica actual',
        categoria='consultoria',
        duracion_estimada_horas=40
    )
    servicio2 = Servicio.objects.create(
        nombre='Desarrollo de prototipo',
        descripcion='Creación de prototipo funcional MVP',
        categoria='desarrollo',
        duracion_estimada_horas=120
    )
    print(f"   ✓ Servicio 1: {servicio1.nombre}")
    print(f"   ✓ Servicio 2: {servicio2.nombre}")
else:
    servicio1 = Servicio.objects.first()
    servicio2 = Servicio.objects.all()[1] if Servicio.objects.count() > 1 else servicio1
    print(f"   ℹ Servicios ya existen")

# Profesional
if not Profesional.objects.exists():
    profesional = Profesional.objects.create(
        run='12.345.678-9',
        nombres='Juan Carlos',
        apellidos='González Pérez',
        especialidad='Desarrollo de Software',
        email='jgonzalez@inacap.cl'
    )
    print(f"   ✓ Profesional: {profesional.nombres} {profesional.apellidos}")
else:
    profesional = Profesional.objects.first()
    print(f"   ℹ Profesional ya existe: {profesional.nombres} {profesional.apellidos}")

# Orden de Servicio
if not OrdenServicio.objects.exists():
    orden = OrdenServicio.objects.create(
        empresa=empresa,
        estado='pendiente',
        prioridad='media',
        descripcion_requerimiento='Modernización de sistemas legacy',
        profesional_asignado=profesional
    )
    orden.servicios_seleccionados.add(servicio1, servicio2)
    print(f"   ✓ Orden de Servicio: #{orden.id}")
else:
    print(f"   ℹ Órdenes de servicio ya existen")

print()
print("=" * 60)
print("✓ PROYECTO INICIALIZADO CORRECTAMENTE")
print("=" * 60)
print()
print("Próximos pasos:")
print("1. Ejecuta: python manage.py runserver")
print("2. Abre: http://127.0.0.1:8000/")
print("3. Login con: admin / admin123")
print()
print("Resumen de datos creados:")
print(f"  - Usuarios: {User.objects.count()}")
print(f"  - Empresas: {Empresa.objects.count()}")
print(f"  - Servicios: {Servicio.objects.count()}")
print(f"  - Profesionales: {Profesional.objects.count()}")
print(f"  - Órdenes: {OrdenServicio.objects.count()}")
print()
