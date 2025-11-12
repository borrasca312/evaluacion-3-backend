# Sistema de Gestión de Asistencias Técnicas (INACAP Biobío)

Proyecto Django para la Evaluación N°3 (Programación Backend).

**Repositorio GitHub**: https://github.com/borrasca312/evaluacion-3-backend

## Requisitos mínimos
- Python 3.10+
- Django 4.2+

## 🚀 Instalación rápida (desde GitHub)

### Paso 1: Clonar o descargar el repositorio
```powershell
# Opción A: Clonar con Git
git clone https://github.com/borrasca312/evaluacion-3-backend.git
cd evaluacion-3-backend

# Opción B: Descargar ZIP desde GitHub
# 1. Ir a https://github.com/borrasca312/evaluacion-3-backend
# 2. Click en "Code" > "Download ZIP"
# 3. Extraer y abrir terminal en la carpeta
```

### Paso 2: Crear entorno virtual e instalar dependencias
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Paso 3: Crear base de datos y datos iniciales
```powershell
python manage.py migrate
python init_project.py
```

El script `init_project.py` creará automáticamente:
- ✅ Usuario admin con contraseña `admin123`
- ✅ Datos de ejemplo (empresas, servicios, profesionales, órdenes)

### Paso 4: Iniciar servidor
```powershell
python manage.py runserver
```

### 🔐 Credenciales de acceso
- **Usuario**: `admin`
- **Contraseña**: `admin123`
- **Login**: http://127.0.0.1:8000/accounts/login/
- **Admin Django**: http://127.0.0.1:8000/admin/

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
