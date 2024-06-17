from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import GuiaQuirurgicaForm, ModeloForm, BiomodeloForm
from trabajos.forms import TrabajoForm
from pacientes.forms import PacienteForm
from doctores.forms import DoctorForm
from .models import TrabajoImpresion3D, GuiaQuirurgica, Modelo, Biomodelo
from trabajos.models import Trabajo
from pacientes.models import Paciente
from doctores.models import Doctor
from pacientes.rut_generico import RutGenerator

def crear_trabajo_impresion3d(request):
    if request.method == 'POST':
        trabajo_form = TrabajoForm(request.POST, prefix='trabajo')
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        doctor_form = DoctorForm(request.POST, prefix='doctor')
        tipo_impresion = request.POST.get('tipo_impresion_3d')
        
        guia_form = GuiaQuirurgicaForm(request.POST, prefix='guia')
        modelo_form = ModeloForm(request.POST, prefix='modelo')
        biomodelo_form = BiomodeloForm(request.POST, prefix='biomodelo')

        if trabajo_form.is_valid() and paciente_form.is_valid() and doctor_form.is_valid():
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
            trabajo.tipo_trabajo = 'impresion_3d'
            trabajo.estado = 'en_proceso'
            trabajo.save()

            trabajo_impresion3d = TrabajoImpresion3D.objects.create(trabajo=trabajo)

            if tipo_impresion == 'guia_quirurgica' and guia_form.is_valid():
                guia = guia_form.save(commit=False)
                guia.trabajo_impresion3d = trabajo_impresion3d
                guia.save()
            elif tipo_impresion == 'modelo' and modelo_form.is_valid():
                modelo = modelo_form.save(commit=False)
                modelo.trabajo_impresion3d = trabajo_impresion3d
                modelo.save()
            elif tipo_impresion == 'biomodelo' and biomodelo_form.is_valid():
                biomodelo = biomodelo_form.save(commit=False)
                biomodelo.trabajo_impresion3d = trabajo_impresion3d
                biomodelo.save()

            return JsonResponse({'success': True, 'redirect': 'seleccionar_tipo_trabajo'})  # Respuesta exitosa para AJAX

    else:
        trabajo_form = TrabajoForm(prefix='trabajo')
        paciente_form = PacienteForm(prefix='paciente')
        doctor_form = DoctorForm(prefix='doctor')
        guia_form = GuiaQuirurgicaForm(prefix='guia')
        modelo_form = ModeloForm(prefix='modelo')
        biomodelo_form = BiomodeloForm(prefix='biomodelo')
        
                                        #         <option value="guia_quirurgica">Guía Quirúrgica</option>
                                        # <option value="modelo">Modelo</option>
                                        # <option value="biomodelo">Biomodelo</option>
    tipos_impresion3d = [
        {
            'value': 'guia_quirurgica',
            'nombre': 'Guía Quirúrgica'
        },
        {
            'value': 'modelo',
            'nombre': 'Modelo'
        },
        {
            'value': 'biomodelo',
            'nombre': 'Biomodelo'
        },
    ]

    return render(request, 'trabajos/crear_trabajo_impresion3d.html', {
        'trabajo_form': trabajo_form,
        'paciente_form': paciente_form,
        'doctor_form': doctor_form,
        'guia_form': guia_form,
        'modelo_form': modelo_form,
        'biomodelo_form': biomodelo_form,
        'tipos_impresion3d': tipos_impresion3d
    })
