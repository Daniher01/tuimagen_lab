from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor


# Create your views here.
@login_required
def buscar_doctor(request):
    lista_doctores = Doctor.objects.all()
    pagado_param = request.GET.get('pagado', 'false').lower()  # Obtener el parámetro de consulta 'pagado'
    pagado = pagado_param == 'true'  # Convertir la cadena a booleano
    
    if request.method == 'POST':
        nombre_doctor = request.POST.get('nombre_doctor')
        pagado = request.POST.get('pagado') == 'true'  # Convertir el valor a booleano
        try:
            doctor = Doctor.objects.get(name=nombre_doctor)
            if pagado:
                return redirect('trabajos_pagados_por_doctor', doctor_id=doctor.id)
            else:
                return redirect('trabajos_por_pagar_por_doctor', doctor_id=doctor.id)
        except Doctor.DoesNotExist:
            messages.error(request, 'No se encontró un doctor con ese nombre. Por favor, intente nuevamente.')
    
    return render(request, 'trabajos/buscar_doctor.html', {'lista_doctores': lista_doctores, 'pagado': pagado})


