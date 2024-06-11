from django.contrib import admin
from .models import TrabajoFresado, Pieza

class PiezaInline(admin.TabularInline):
    model = Pieza
    extra = 1

@admin.register(TrabajoFresado)
class TrabajoFresadoAdmin(admin.ModelAdmin):
    list_display = ('trabajo', 'con_maquillaje')
    inlines = [PiezaInline]
