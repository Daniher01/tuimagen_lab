from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.http import JsonResponse
from django.utils import timezone
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
@login_required
def seleccionar_tipo_trabajo(request):
    tipos_trabajo = Trabajo.TIPOS
    return render(request, 'trabajos/menu.html', {'tipos': tipos_trabajo})

@login_required
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

@login_required
@require_POST
@csrf_exempt
def terminar_trabajo(request):
    ESTADO = 'terminado'
    trabajo_id = request.POST.get('id')
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    
    if trabajo.estado != ESTADO:
        trabajo.estado = ESTADO
        trabajo.fecha_termino = timezone.now()
        trabajo.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'El trabajo ya está terminado'})