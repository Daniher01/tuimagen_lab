from django.db import models
from django.utils import timezone
from pacientes.models import Paciente
from doctores.models import Doctor

class Trabajo(models.Model):
    ESTADOS = [
        ('en_proceso', 'En proceso'),
        ('terminado', 'Terminado'),
    ]

    TIPOS = [
        ('fresado', 'Fresado'),
        ('impresion_3d', 'Impresión 3D'),
        ('escaneo_intraoral', 'Escaneo Intraoral'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_entrega = models.DateField()
    fecha_termino = models.DateField(null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='en_proceso')
    tipo_trabajo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return f'Trabajo {self.tipo_trabajo} para {self.paciente}'

