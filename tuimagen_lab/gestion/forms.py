from django import forms
from .models import Trabajo, TrabajoPieza, Paciente, Dentista, Material

class DateInput(forms.DateInput):
    input_type = 'date'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre']

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['fecha_entrega', 'dentista']
        exclude = ['estado', 'paciente']
        widgets = {
            'fecha_entrega': DateInput(),
        }

class TrabajoPiezaForm(forms.ModelForm):
    class Meta:
        model = TrabajoPieza
        fields = ['pieza', 'material']
