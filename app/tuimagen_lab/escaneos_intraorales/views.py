from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import EscaneoIntraoralForm
from trabajos.forms import TrabajoForm
from pacientes.forms import PacienteForm
from doctores.forms import DoctorForm
from .models import EscaneoIntraoral, Trabajo
from doctores.models import Doctor
from pacientes.models import Paciente
from pacientes.rut_generico import RutGenerator

@login_required
def crear_trabajo_escaneo_intraoral(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        doctor_form = DoctorForm(request.POST, prefix='doctor')
        trabajo_form = TrabajoForm(request.POST, prefix='trabajo')
        escaneo_form = EscaneoIntraoralForm(request.POST, prefix='escaneo')

        if (paciente_form.is_valid() and doctor_form.is_valid() and trabajo_form.is_valid() and escaneo_form.is_valid()):
            paciente_rut = paciente_form.cleaned_data['rut']
            paciente_nombre = paciente_form.cleaned_data['name']
            doctor_nombre = doctor_form.cleaned_data['name']
            
            if paciente_rut == 'Sin Rut':
                generator = RutGenerator()
                nuevo_rut = generator.generate_unique_rut()
                paciente_rut = nuevo_rut
                
            paciente, created = Paciente.objects.get_or_create(rut=paciente_rut)
            paciente.name = paciente_nombre
            paciente.save()

            doctor, created = Doctor.objects.get_or_create(name=doctor_nombre)
            
            trabajo = trabajo_form.save(commit=False)
            trabajo.paciente = paciente
            trabajo.doctor = doctor
            trabajo.tipo_trabajo = 'escaneo_intraoral'
            trabajo.estado = 'en_proceso'
            trabajo.save()

            escaneo = escaneo_form.save(commit=False)
            escaneo.trabajo = trabajo
            escaneo.save()
            

            return JsonResponse({'success': True, 'redirect': 'listar_trabajos_pendientes'})
    else:
        paciente_form = PacienteForm(prefix='paciente')
        doctor_form = DoctorForm(prefix='doctor')
        trabajo_form = TrabajoForm(prefix='trabajo')
        escaneo_form = EscaneoIntraoralForm(prefix='escaneo')

    lista_doctores = Doctor.objects.all()
    return render(request, 'trabajos/crear_trabajo_escaneo_intraoral.html', {
        # formularios
        'paciente_form': paciente_form,
        'doctor_form': doctor_form,
        'trabajo_form': trabajo_form,
        'escaneo_form': escaneo_form,
        # datos para los formularios
        'lista_doctores': lista_doctores
    })

@login_required
def detalle_trabajo_escaneo_intraoral(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id, tipo_trabajo='escaneo_intraoral')
    escaneo = get_object_or_404(EscaneoIntraoral, trabajo=trabajo)

    ESTADOS = dict(Trabajo.ESTADOS)

    data = {
        'trabajo_id': trabajo.id,
        'paciente_nombre': trabajo.paciente.name,
        'paciente_rut': trabajo.paciente.rut,
        'doctor_nombre': trabajo.doctor.name,
        'fecha_ingreso': trabajo.fecha_creacion.strftime('%d-%m-%Y'),
        'fecha_entrega': trabajo.fecha_entrega.strftime('%d-%m-%Y'),
        'estado': ESTADOS.get(trabajo.estado, trabajo.estado),
        'tipo_escaneo': escaneo.tipo_escaneo,
        'lugar_escaneo': escaneo.lugar_escaneo,
    }

    return JsonResponse(data)