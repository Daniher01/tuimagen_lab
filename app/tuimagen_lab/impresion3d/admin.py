from django.contrib import admin
from .models import TrabajoImpresion3D, GuiaQuirurgica, Modelo, Biomodelo

class GuiaQuirurgicaInline(admin.TabularInline):
    model = GuiaQuirurgica
    extra = 1

class ModeloInline(admin.TabularInline):
    model = Modelo
    extra = 1

class BiomodeloInline(admin.TabularInline):
    model = Biomodelo
    extra = 1

@admin.register(TrabajoImpresion3D)
class TrabajoImpresion3DAdmin(admin.ModelAdmin):
    list_display = ('trabajo',)
    inlines = [GuiaQuirurgicaInline, ModeloInline, BiomodeloInline]
