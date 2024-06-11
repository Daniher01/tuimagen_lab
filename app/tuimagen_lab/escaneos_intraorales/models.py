from django.db import models
from trabajos.models import Trabajo

class EscaneoIntraoral(models.Model):
    TIPOS_ESCANEO = [
        ('superior', 'Superior'),
        ('inferior', 'Inferior'),
        ('ambos', 'Ambos'),
        ('hemiarcada', 'Hemiarcada'),
    ]

    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)
    tipo_escaneo = models.CharField(max_length=20, choices=TIPOS_ESCANEO)
    lugar_escaneo = models.CharField(max_length=255)

    def __str__(self):
        return f'Escaneo intraoral {self.tipo_escaneo} para {self.trabajo.paciente}'
