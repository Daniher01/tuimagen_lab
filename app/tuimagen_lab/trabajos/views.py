from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.db.models import Count
from .models import Trabajo, TrabajoDoctor
from doctores.models import Doctor



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
def ver_trabajos_terminados(request):
    ESTADO = 'terminado'

    # Obtener fechas desde el formulario
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if fecha_desde and fecha_hasta:
        # Convertir las fechas de cadena a objetos de fecha
        fecha_desde = parse_date(fecha_desde)
        fecha_hasta = parse_date(fecha_hasta)

        # Asegurarse de que la fecha_hasta incluye todo el día
        fecha_hasta = fecha_hasta + timedelta(days=1)

        # Filtrar los trabajos por las fechas proporcionadas
        trabajos = Trabajo.objects.filter(estado=ESTADO, fecha_termino__range=(fecha_desde, fecha_hasta))
    else:
        # Filtrar los trabajos terminados en los últimos 30 días si no se proporcionan fechas
        hace_30_dias = datetime.now() - timedelta(days=30)
        trabajos = Trabajo.objects.filter(estado=ESTADO, fecha_termino__gte=hace_30_dias)

    # Obtener el total de trabajos agrupados por tipo de trabajo
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

@login_required
def trabajos_por_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    trabajos_doctor = TrabajoDoctor.objects.filter(doctor=doctor)
    context = {
        'doctor': doctor,
        'trabajos_doctor': trabajos_doctor,
    }
    return render(request, 'trabajos/trabajos_por_doctor.html', context)

@login_required
def buscar_doctor(request):
    lista_doctores = Doctor.objects.all()
    
    if request.method == 'POST':
        nombre_doctor = request.POST.get('nombre_doctor')
        try:
            doctor = Doctor.objects.get(name=nombre_doctor)
            return redirect('trabajos_por_doctor', doctor_id=doctor.id)
        except Doctor.DoesNotExist:
            messages.error(request, 'No se encontró un doctor con ese nombre. Por favor, intente nuevamente.')
    return render(request, 'trabajos/buscar_doctor.html', {'lista_doctores': lista_doctores})