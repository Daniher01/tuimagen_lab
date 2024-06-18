from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from trabajos.forms import TrabajoForm
from fresado.forms import PiezaForm
from pacientes.forms import PacienteForm
from doctores.forms import DoctorForm
from django.forms import inlineformset_factory
from fresado.models import TrabajoFresado, Pieza
from pacientes.models import Paciente
from doctores.models import Doctor
from trabajos.models import Trabajo
from pacientes.rut_generico import RutGenerator

@login_required
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

            # verifica y el paciente tiene o no un rut
            if paciente_rut == 'Sin Rut':
                generator = RutGenerator()
                nuevo_rut = generator.generate_unique_rut()
                paciente_rut = nuevo_rut

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
        
    lista_doctores = Doctor.objects.all()

    return render(request, 'trabajos/crear_trabajo_fresado.html', {
        # formularios
        'trabajo_form': trabajo_form,
        'pieza_formset': pieza_formset,
        'paciente_form': paciente_form,
        'doctor_form': doctor_form,
        # datos para los formularios
        'lista_doctores': lista_doctores
    })

@login_required
def detalle_trabajo_fresado(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id, tipo_trabajo='fresado')
    fresado = get_object_or_404(TrabajoFresado, trabajo=trabajo)
    piezas = Pieza.objects.filter(trabajo_fresado=fresado)

    data = {
        'id_trabajo': trabajo.id,
        'paciente_nombre': trabajo.paciente.name,
        'paciente_rut': trabajo.paciente.rut,
        'doctor_nombre': trabajo.doctor.name,
        'fecha_ingreso': trabajo.fecha_creacion.strftime('%d-%m-%Y'),
        'fecha_entrega': trabajo.fecha_entrega.strftime('%d-%m-%Y'),
        'estado': trabajo.get_estado_display(),
        'con_maquillaje': fresado.con_maquillaje,
        'piezas': [{'tipo': pieza.tipo_pieza, 'material': pieza.material, 'bloque': pieza.bloque} for pieza in piezas]
    }

    return JsonResponse(data)