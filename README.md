# Sistema de Gestión de Asistencias Técnicas (INACAP Biobío)

Proyecto Django para la Evaluación N°3 (Programación Backend).

## Requisitos mínimos
- Python 3.10+
- Django 4.2+

## Instalación rápida

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Credenciales de prueba
- **Usuario admin**: `admin`
- **Contraseña**: `admin123`
- **Acceso al admin**: http://127.0.0.1:8000/admin/

El proyecto contiene la app `core` con los modelos Empresa, Servicio, Profesional y OrdenServicio y CRUD básico.

### URLs disponibles
- http://127.0.0.1:8000/ - Listado de órdenes de servicio
- http://127.0.0.1:8000/empresas/ - Listado de empresas
- http://127.0.0.1:8000/servicios/ - Listado de servicios
- http://127.0.0.1:8000/profesionales/ - Listado de profesionales
- http://127.0.0.1:8000/admin/ - Panel de administración Django
- http://127.0.0.1:8000/accounts/login/ - Login

### Datos de prueba incluidos
El sistema incluye datos de ejemplo:
- 1 Empresa: PYME Ejemplo S.A.
- 2 Servicios: Diagnóstico tecnológico, Desarrollo de prototipo
- 1 Profesional: Juan Carlos González Pérez
- 1 Orden de Servicio activa

## Características implementadas

### Modelos ORM
- *Empresa*: RUT único, razón social, giro, teléfono, email, dirección, comuna
- **Servicio*: Nombre único, descripción, categoría, duración estimada, activo
- **Profesional**: RUN único, nombres, apellidos, especialidad, email  
- **OrdenServicio**: Relaciones con Empresa (1-N), Servicio (M-M), Profesional (1-N)

### CRUD completo
- Listar, crear, ver detalle, actualizar y eliminar para todas las entidades
- Protección con LoginRequired para operaciones de escritura

### Admin
- Configurado con list_display, list_filter, search_fields, ordering
- Acciones masivas para cambiar estado de OrdenServicio

### Autenticación
- Sistema de login/logout integrado
- Sesiones para operaciones protegidas
