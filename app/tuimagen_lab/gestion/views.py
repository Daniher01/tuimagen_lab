from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Trabajo, TrabajoPieza, Paciente, Dentista
from .forms import TrabajoForm, TrabajoPiezaForm, PacienteForm, DentistaForm

@login_required
def crear_trabajo(request):
    TrabajoPiezaFormSet = modelformset_factory(TrabajoPieza, form=TrabajoPiezaForm, extra=1)
    
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        dentista_form = DentistaForm(request.POST, prefix='dentista')
        trabajo_form = TrabajoForm(request.POST, prefix='trabajo')
        trabajo_pieza_formset = TrabajoPiezaFormSet(request.POST, queryset=TrabajoPieza.objects.none(), prefix='trabajo_pieza')

        if paciente_form.is_valid() and dentista_form.is_valid() and trabajo_form.is_valid() and trabajo_pieza_formset.is_valid():
            paciente_rut = paciente_form.cleaned_data['rut']
            paciente_nombre = paciente_form.cleaned_data['nombre']
            paciente, created = Paciente.objects.update_or_create(rut=paciente_rut, defaults={'nombre': paciente_nombre})
            
            dentista_nombre = dentista_form.cleaned_data['nombre']
            dentista, created = Dentista.objects.update_or_create(nombre=dentista_nombre)
            
            trabajo = trabajo_form.save(commit=False)
            trabajo.paciente = paciente
            trabajo.dentista = dentista
            trabajo.estado = 'EN_PROCESO'
            trabajo.save()

            for form in trabajo_pieza_formset:
                if form.cleaned_data:
                    trabajo_pieza = form.save(commit=False)
                    trabajo_pieza.trabajo = trabajo
                    trabajo_pieza.save()
            return redirect('detalle_trabajo', trabajo_id=trabajo.id)
    else:
        paciente_form = PacienteForm(prefix='paciente')
        dentista_form = DentistaForm(prefix='dentista')
        trabajo_form = TrabajoForm(prefix='trabajo')
        trabajo_pieza_formset = TrabajoPiezaFormSet(queryset=TrabajoPieza.objects.none(), prefix='trabajo_pieza')

    return render(request, 'gestion/crear_trabajo.html', {
        'paciente_form': paciente_form,
        'dentista_form': dentista_form,
        'trabajo_form': trabajo_form,
        'trabajo_pieza_formset': trabajo_pieza_formset,
    })

@login_required
def listar_trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, 'gestion/listar_trabajos.html', {'trabajos': trabajos})

@login_required
def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    return render(request, 'gestion/detalle_trabajo.html', {'trabajo': trabajo})