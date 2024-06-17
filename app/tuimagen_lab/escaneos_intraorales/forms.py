from django import forms
from .models import EscaneoIntraoral

class EscaneoIntraoralForm(forms.ModelForm):
    class Meta:
        model = EscaneoIntraoral
        fields = ['tipo_escaneo', 'lugar_escaneo']
        widgets = {
            'tipo_escaneo': forms.Select(attrs={'class': 'form-select'}),
            'lugar_escaneo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar de Escaneo'}),
        }
