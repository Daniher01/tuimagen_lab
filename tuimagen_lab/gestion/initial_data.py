from .models import Pieza, Material
from .choices import PIEZAS, MATERIALES

def create_initial_piezas(sender, **kwargs):
    for pieza in PIEZAS:
        Pieza.objects.get_or_create(nombre=pieza[0])
    
def create_initial_materiales(sender, **kwargs):
    for material in MATERIALES:
        Material.objects.get_or_create(nombre=material[0])