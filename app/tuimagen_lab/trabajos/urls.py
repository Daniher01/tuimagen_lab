from django.urls import path
from .views import seleccionar_tipo_trabajo

urlpatterns = [
    path('', seleccionar_tipo_trabajo, name='seleccionar_tipo_trabajo'),
    # Agrega las URLs para la creación de los trabajos
    path('crear-trabajo-fresado/', seleccionar_tipo_trabajo, name='crear_trabajo_fresado'),
    path('crear-trabajo-impresion3d/', seleccionar_tipo_trabajo, name='crear_trabajo_impresion3d'),
    path('crear-trabajo-escaneo-intraoral/', seleccionar_tipo_trabajo, name='crear_trabajo_escaneo_intraoral'),
]
