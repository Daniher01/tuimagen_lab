from django.shortcuts import render

# Create your views here.
def seleccionar_tipo_trabajo(request):
    return render(request, 'trabajos/menu.html')