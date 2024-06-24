from django.urls import path
from .views import seleccionar_tipo_trabajo, ver_trabajos_pendientes
from fresado import views as fresado
from impresion3d import views as impresion3d
from escaneos_intraorales import views as escaner_intraoral

urlpatterns = [
    path('', seleccionar_tipo_trabajo, name='seleccionar_tipo_trabajo'),
    path('pendientes/', ver_trabajos_pendientes, name='trabajos_pendientes'),
    # URLs para la creación de los trabajos
    path('crear-trabajo-fresado/', fresado.crear_trabajo_fresado, name='crear_trabajo_fresado'),
    path('crear-trabajo-impresion3d/', impresion3d.crear_trabajo_impresion3d, name='crear_trabajo_impresion3d'),
    path('crear-trabajo-escaneo-intraoral/', escaner_intraoral.crear_trabajo_escaneo_intraoral, name='crear_trabajo_escaneo_intraoral'),
    # URLs para el detallsd de los trabajos
    path('detalle/fresado/<int:trabajo_id>', fresado.detalle_trabajo_fresado, name='detalle_trabajo_fresado'),
    path('detalle/impresion3d/<int:trabajo_id>', impresion3d.detalle_trabajo_impresion3d, name='detalle_trabajo_impresion3d'),
    path('detalle/escaneo_intraoral/<int:trabajo_id>/', escaner_intraoral.detalle_trabajo_escaneo_intraoral, name='detalle_trabajo_escaneo_intraoral'),
]
