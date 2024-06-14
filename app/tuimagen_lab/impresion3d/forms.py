# forms.py
from django import forms
from .models import GuiaQuirurgica, Modelo, Biomodelo

class GuiaQuirurgicaForm(forms.ModelForm):
    class Meta:
        model = GuiaQuirurgica
        fields = ['descripcion']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['descripcion', 'tipo']

class BiomodeloForm(forms.ModelForm):
    class Meta:
        model = Biomodelo
        fields = ['descripcion']
