from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TrabajoForm
from fresado.forms import PiezaForm
from pacientes.forms import PacienteForm
from doctores.forms import DoctorForm
from django.forms import inlineformset_factory
from .models import Trabajo
from fresado.models import TrabajoFresado, Pieza
from pacientes.models import Paciente
from doctores.models import Doctor
from pacientes.rut_generico import RutGenerator

# Create your views here.
def seleccionar_tipo_trabajo(request):
    tipos_trabajo = Trabajo.TIPOS
    return render(request, 'trabajos/menu.html', {'tipos': tipos_trabajo})