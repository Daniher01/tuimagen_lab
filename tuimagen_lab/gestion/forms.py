from django import forms
from .models import Trabajo, TrabajoPieza, Paciente, Dentista

class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista
        fields = ['nombre']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'rut']

class DateInput(forms.DateInput):
    input_type = 'date'

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['fecha_entrega']
        exclude = ['estado', 'paciente', 'dentista']  # Excluir 'dentista' si se maneja por separado
        widgets = {
            'fecha_entrega': DateInput(),
        }

class TrabajoPiezaForm(forms.ModelForm):
    class Meta:
        model = TrabajoPieza
        fields = ['pieza', 'material']
