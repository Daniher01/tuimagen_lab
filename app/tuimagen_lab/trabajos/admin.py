from django.contrib import admin
from .models import Trabajo, TrabajoDoctor

@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'fecha_entrega',  'estado', 'tipo_trabajo')
    search_fields = ('paciente__name', 'doctor__name', 'tipo_trabajo')
    list_filter = ('estado', 'tipo_trabajo')

@admin.register(TrabajoDoctor)
class TrabajoDoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'trabajo', 'pagado', 'fecha_pago')
    list_filter = ('doctor', 'pagado')
    search_fields = ('doctor__name', 'trabajo__tipo_trabajo')