from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor


# Create your views here.
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