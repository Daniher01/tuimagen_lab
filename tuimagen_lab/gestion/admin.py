from django.contrib import admin
from .models import Paciente, Dentista, Material, Pieza, Trabajo, TrabajoPieza

admin.site.register(Paciente)
admin.site.register(Dentista)
admin.site.register(Material)
admin.site.register(Pieza)
admin.site.register(Trabajo)
admin.site.register(TrabajoPieza)
