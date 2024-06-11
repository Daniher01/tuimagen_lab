from django.contrib import admin
from .models import Trabajo

@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'fecha_entrega',  'estado', 'tipo_trabajo')
    search_fields = ('paciente__name', 'doctor__name', 'tipo_trabajo')
    list_filter = ('estado', 'tipo_trabajo')
