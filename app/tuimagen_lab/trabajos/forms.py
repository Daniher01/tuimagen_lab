from django import forms
from .models import Trabajo

class DateInput(forms.DateInput):
    input_type = 'date'

class TrabajoForm(forms.ModelForm):
    con_maquillaje = forms.BooleanField(required=False, label='Con Maquillaje')
    
    class Meta:
        model = Trabajo
        fields = ['fecha_entrega']
        widgets = {
            'fecha_entrega': DateInput(),
        }
