from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'rut')
    search_fields = ('name', 'rut')
