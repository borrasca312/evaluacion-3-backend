from django.core.validators import MinValueValidator, EmailValidator
from django.db import models
from django.core.exceptions import ValidationError

"""
Modelos ORM para el Sistema de Gestión de Asistencias Técnicas INACAP Biobío.

Relaciones principales:
  - Empresa (1) --> (N) OrdenServicio (ForeignKey con CASCADE)
  - Profesional (1) --> (N) OrdenServicio (ForeignKey con SET_NULL, opcional)
  - Servicio (N) <--> (N) OrdenServicio (ManyToMany, sin límite)
"""


class Empresa(models.Model):
    """
    Representa una empresa cliente que solicita servicios técnicos.
    
    Atributos:
        rut: Identificador único de la empresa (máx 12 caracteres).
        razon_social: Nombre legal de la empresa (requerido).
        email: Correo de contacto (validado automáticamente por EmailField).
    """
    rut = models.CharField(max_length=12, unique=True)
    razon_social = models.CharField(max_length=200)
    giro = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=250, blank=True)
    comuna = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.razon_social} ({self.rut})"

    def clean(self):
        # Basic validations: razon_social required (enforced by non blank) and email format handled by EmailField
        if not self.razon_social:
            raise ValidationError({'razon_social': 'La razón social es obligatoria.'})


class Servicio(models.Model):
    """
    Representa un servicio técnico ofrecido por la empresa.
    
    Atributos:
        nombre: Nombre único del servicio (ej: "Diagnóstico tecnológico").
        duracion_estimada_horas: Tiempo estimado (validado con MinValueValidator(0)).
        activo: Indica si el servicio está disponible para nuevas órdenes.
    """
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    duracion_estimada_horas = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    """
    Representa un técnico/profesional que ejecuta servicios.
    
    Atributos:
        run: Identificador único del profesional (RUN chileno, máx 12 caracteres).
        nombres, apellidos: Datos de identidad.
        especialidad: Área de expertise (ej: "Reparación de hardware").
    """
    run = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.run})"


class OrdenServicio(models.Model):
    """
    Representa una orden de servicio que vincula una Empresa con uno o más Servicios.
    
    Relaciones:
        - Empresa (ForeignKey, CASCADE): Si se elimina la empresa, se eliminan sus órdenes.
        - Servicios (ManyToMany): Una orden puede solicitar múltiples servicios.
        - Profesional (ForeignKey, SET_NULL): Técnico asignado (puede quedar vacío).
    
    Estados de la orden:
        - 'nueva': Orden recién creada, sin asignación.
        - 'en_ejecucion': Profesional está trabajando en ella.
        - 'finalizada': Trabajo completado.
        - 'cancelada': Orden cancelada.
    
    Prioridad:
        - 'baja': Trabajo no urgente.
        - 'media': Prioridad normal.
        - 'alta': Trabajo urgente.
    """
    ESTADO_CHOICES = [
        ('nueva', 'Nueva'),
        ('en_ejecucion', 'En ejecución'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='ordenes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nueva')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    descripcion_requerimiento = models.TextField(blank=True)
    servicios_seleccionados = models.ManyToManyField(Servicio, blank=True, related_name='ordenes')
    profesional_asignado = models.ForeignKey(Profesional, null=True, blank=True, on_delete=models.SET_NULL, related_name='ordenes')

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Orden #{self.id} - {self.empresa} - {self.get_estado_display()}"

    def clean(self):
        """
        Validación personalizada: puede extenderse para verificar reglas de negocio.
        Ejemplo: una orden finalizada debe tener un profesional asignado.
        """
        if self.estado == 'finalizada':
            pass
