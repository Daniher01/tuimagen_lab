from django.shortcuts import render, redirect
from django.db.models import Count
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

def ver_trabajos_pendientes(request):
    ESTADO = 'en_proceso'
    trabajos = Trabajo.objects.filter(estado=ESTADO)
    total_trabajos = trabajos.values('tipo_trabajo').annotate(total=Count('tipo_trabajo'))
    
    # cambiar los valores del nombre de los tipos de trabajo
    TIPOS_DICT = {key: value for key, value in Trabajo.TIPOS}
    # Reemplazar 'tipo_trabajo' en el queryset
    for item in total_trabajos:
        item['tipo_trabajo'] = TIPOS_DICT.get(item['tipo_trabajo'], item['tipo_trabajo'])
  
    return render(request, 'trabajos/listar_trabajos.html', {'trabajos': trabajos, 'total_trabajos': total_trabajos, 'estado': ESTADO})