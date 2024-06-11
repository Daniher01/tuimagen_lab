from django import forms
from .models import Pieza

class PiezaForm(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['material', 'tipo_pieza', 'bloque']