from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .models import Trabajo, TrabajoPieza, Paciente
from .forms import TrabajoForm, TrabajoPiezaForm, PacienteForm

def crear_trabajo(request):
    TrabajoPiezaFormSet = modelformset_factory(TrabajoPieza, form=TrabajoPiezaForm, extra=1)
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        trabajo_form = TrabajoForm(request.POST)
        trabajo_pieza_formset = TrabajoPiezaFormSet(request.POST, queryset=TrabajoPieza.objects.none())

        if paciente_form.is_valid() and trabajo_form.is_valid() and trabajo_pieza_formset.is_valid():
            paciente = paciente_form.save()
            trabajo = trabajo_form.save(commit=False)
            trabajo.paciente = paciente
            trabajo.estado = 'EN_PROCESO'
            trabajo.save()
            for form in trabajo_pieza_formset:
                if form.cleaned_data:
                    trabajo_pieza = form.save(commit=False)
                    trabajo_pieza.trabajo = trabajo
                    trabajo_pieza.save()
            return redirect('detalle_trabajo', trabajo_id=trabajo.id)
    else:
        paciente_form = PacienteForm()
        trabajo_form = TrabajoForm()
        trabajo_pieza_formset = TrabajoPiezaFormSet(queryset=TrabajoPieza.objects.none())

    return render(request, 'gestion/crear_trabajo.html', {
        'paciente_form': paciente_form,
        'trabajo_form': trabajo_form,
        'trabajo_pieza_formset': trabajo_pieza_formset,
    })

def listar_trabajos(request):
    trabajos = Trabajo.objects.all()
    return render(request, 'gestion/listar_trabajos.html', {'trabajos': trabajos})

def detalle_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    return render(request, 'gestion/detalle_trabajo.html', {'trabajo': trabajo})
