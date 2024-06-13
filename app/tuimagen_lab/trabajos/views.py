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

# Create your views here.
def seleccionar_tipo_trabajo(request):
    tipos_trabajo = Trabajo.TIPOS
    return render(request, 'trabajos/menu.html', {'tipos': tipos_trabajo})

def crear_trabajo_fresado(request):
    PiezaFormSet = inlineformset_factory(TrabajoFresado, Pieza, form=PiezaForm, extra=1, can_delete=False)

    if request.method == 'POST':
        trabajo_form = TrabajoForm(request.POST, prefix='trabajo')
        pieza_formset = PiezaFormSet(request.POST, prefix='pieza')
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        doctor_form = DoctorForm(request.POST, prefix='doctor')

        # Validar todos los formularios
        if trabajo_form.is_valid() and pieza_formset.is_valid() and paciente_form.is_valid() and doctor_form.is_valid():
            # Obtener los datos limpios
            paciente_rut = paciente_form.cleaned_data['rut']
            paciente_nombre = paciente_form.cleaned_data['name']
            doctor_nombre = doctor_form.cleaned_data['name']

            # Crear o actualizar paciente
            paciente, created = Paciente.objects.get_or_create(rut=paciente_rut)
            paciente.name = paciente_nombre
            paciente.save()

            # Crear o actualizar doctor
            doctor, created = Doctor.objects.get_or_create(name=doctor_nombre)

            # Crear trabajo
            trabajo = trabajo_form.save(commit=False)
            trabajo.paciente = paciente
            trabajo.doctor = doctor
            trabajo.tipo_trabajo = 'fresado'
            trabajo.estado = 'en_proceso'
            trabajo.save()

            # Crear trabajo de fresado
            trabajo_fresado = TrabajoFresado.objects.create(
                trabajo=trabajo,
                con_maquillaje=trabajo_form.cleaned_data['con_maquillaje']
            )

            # Guardar piezas
            piezas = pieza_formset.save(commit=False)
            for pieza in piezas:
                pieza.trabajo_fresado = trabajo_fresado
                pieza.save()

            return JsonResponse({'success': True, 'redirect': 'seleccionar_tipo_trabajo'})  # Respuesta exitosa para AJAX
        else:
            # Manejar errores y enviar una respuesta JSON con errores
            errors = {
                'trabajo_form': trabajo_form.errors,
                'pieza_formset': pieza_formset.errors,
                'paciente_form': paciente_form.errors,
                'doctor_form': doctor_form.errors,
            }
            return JsonResponse({'success': False, 'errors': errors})

    else:
        trabajo_form = TrabajoForm(prefix='trabajo')
        pieza_formset = PiezaFormSet(prefix='pieza')
        paciente_form = PacienteForm(prefix='paciente')
        doctor_form = DoctorForm(prefix='doctor')

    return render(request, 'trabajos/crear_trabajo_fresado.html', {
        'trabajo_form': trabajo_form,
        'pieza_formset': pieza_formset,
        'paciente_form': paciente_form,
        'doctor_form': doctor_form,
    })
