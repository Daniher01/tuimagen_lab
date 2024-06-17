from django.urls import path
from .views import seleccionar_tipo_trabajo, ver_trabajos_pendientes
from fresado import views as fresado
from impresion3d import views as impresion3d
from escaneos_intraorales import views as escaner_intraoral

urlpatterns = [
    path('', seleccionar_tipo_trabajo, name='seleccionar_tipo_trabajo'),
    path('pendientes/', ver_trabajos_pendientes, name='trabajos_pendientes'),
    # Agrega las URLs para la creación de los trabajos
    path('crear-trabajo-fresado/', fresado.crear_trabajo_fresado, name='crear_trabajo_fresado'),
    path('crear-trabajo-impresion3d/', impresion3d.crear_trabajo_impresion3d, name='crear_trabajo_impresion3d'),
    path('crear-trabajo-escaneo-intraoral/', escaner_intraoral.crear_trabajo_escaneo_intraoral, name='crear_trabajo_escaneo_intraoral'),
]
