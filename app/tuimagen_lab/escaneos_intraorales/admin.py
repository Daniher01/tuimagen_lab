from django.contrib import admin
from .models import EscaneoIntraoral

@admin.register(EscaneoIntraoral)
class EscaneoIntraoralAdmin(admin.ModelAdmin):
    list_display = ('trabajo', 'tipo_escaneo', 'lugar_escaneo')
    search_fields = ('trabajo__paciente__name', 'tipo_escaneo', 'lugar_escaneo')
    list_filter = ('tipo_escaneo',)
