from django.db import models
from trabajos.models import Trabajo

class TrabajoFresado(models.Model):
    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)
    con_maquillaje = models.BooleanField(default=False)

    def __str__(self):
        return f'Trabajo de fresado para {self.trabajo.paciente}'

class Pieza(models.Model):
    MATERIALES = [
        ('feldespato', 'Feldespato'),
        ('disilicato', 'Disilicato'),
        ('resina', 'Resina'),
    ]
    
    TIPOS_PIEZA = [
        ('1.1', '1.1'),
        ('1.1', '1.2'),
        # Agrega los tipos de pieza según el esquema proporcionado
    ]

    trabajo_fresado = models.ForeignKey(TrabajoFresado, related_name='piezas', on_delete=models.CASCADE)
    tipo_pieza = models.CharField(max_length=50, choices=TIPOS_PIEZA)
    material = models.CharField(max_length=20, choices=MATERIALES)
    bloque = models.CharField(max_length=255)

    def __str__(self):
        return f'Pieza de {self.material}, tipo {self.tipo_pieza}'
