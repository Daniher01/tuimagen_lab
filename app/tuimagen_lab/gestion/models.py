from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

class Dentista(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pieza(models.Model):
    nombre = models.CharField(max_length=5)  # Ejemplo: 1.1, 1.2, etc.

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    ESTADOS = [
        ('EN_PROCESO', 'En proceso'),
        ('TERMINADO', 'Terminado'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)
    fecha_entrega = models.DateField()
    fecha_termino = models.DateField()
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='EN_PROCESO')

    def __str__(self):
        return f'Trabajo {self.id} para: {self.paciente.nombre} con el doctor: {self.dentista.nombre} para el día: {self.fecha_entrega} actualmente está: {self.estado}'

class TrabajoPieza(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='trabajo_piezas')
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f'Trabajo: {self.trabajo.id}, Pieza: {self.pieza.nombre}, Material: {self.material.nombre}'
