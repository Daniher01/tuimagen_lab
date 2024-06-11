from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
