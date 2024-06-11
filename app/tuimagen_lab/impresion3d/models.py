from django.db import models
from trabajos.models import Trabajo

class TrabajoImpresion3D(models.Model):
    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Trabajo de impresión 3D para {self.trabajo.paciente}'

class GuiaQuirurgica(models.Model):
    trabajo_impresion3d = models.ForeignKey(TrabajoImpresion3D, related_name='guias_quirurgicas', on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f'Guía quirúrgica para {self.trabajo_impresion3d.trabajo.paciente}'

class Modelo(models.Model):
    TIPOS_MODELO = [
        ('superior', 'Superior'),
        ('inferior', 'Inferior'),
        ('ambos', 'Ambos'),
        ('hemiarcada', 'Hemiarcada'),
    ]

    trabajo_impresion3d = models.ForeignKey(TrabajoImpresion3D, related_name='modelos', on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS_MODELO)

    def __str__(self):
        return f'Modelo {self.tipo} para {self.trabajo_impresion3d.trabajo.paciente}'

class Biomodelo(models.Model):
    trabajo_impresion3d = models.ForeignKey(TrabajoImpresion3D, related_name='biomodelos', on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f'Biomodelo para {self.trabajo_impresion3d.trabajo.paciente}'
