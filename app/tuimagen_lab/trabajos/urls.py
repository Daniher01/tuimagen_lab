from django.urls import path
from .views import seleccionar_tipo_trabajo, ver_trabajos_pendientes, ver_trabajos_terminados, terminar_trabajo, trabajos_por_pagar_por_doctor, trabajos_pagados_por_doctor, marcar_pagado
from fresado import views as fresado
from impresion3d import views as impresion3d
from escaneos_intraorales import views as escaner_intraoral

urlpatterns = [
    path('', seleccionar_tipo_trabajo, name='seleccionar_tipo_trabajo'),
    path('pendientes/', ver_trabajos_pendientes, name='trabajos_pendientes'),
    path('terminados/', ver_trabajos_terminados, name='trabajos_terminados'),
    path('trabajos-por-pagar/doctor/<int:doctor_id>/', trabajos_por_pagar_por_doctor, name='trabajos_por_pagar_por_doctor'),
    path('trabajos-pagados/doctor/<int:doctor_id>/', trabajos_pagados_por_doctor, name='trabajos_pagados_por_doctor'),
    # URLs para la creación de los trabajos
    path('crear-trabajo-fresado/', fresado.crear_trabajo_fresado, name='crear_trabajo_fresado'),
    path('crear-trabajo-impresion3d/', impresion3d.crear_trabajo_impresion3d, name='crear_trabajo_impresion3d'),
    path('crear-trabajo-escaneo-intraoral/', escaner_intraoral.crear_trabajo_escaneo_intraoral, name='crear_trabajo_escaneo_intraoral'),
    # URLs para el detalles de los trabajos
    path('detalle/fresado/<int:trabajo_id>', fresado.detalle_trabajo_fresado, name='detalle_trabajo_fresado'),
    path('detalle/impresion3d/<int:trabajo_id>', impresion3d.detalle_trabajo_impresion3d, name='detalle_trabajo_impresion3d'),
    path('detalle/escaneo_intraoral/<int:trabajo_id>/', escaner_intraoral.detalle_trabajo_escaneo_intraoral, name='detalle_trabajo_escaneo_intraoral'),
    # URLs para terminar un trabajo
    path('terminar_trabajo/', terminar_trabajo, name='terminar_trabajo'),
    #URLs para pagar los trabajos del doctor
    path('marcar-pagado/', marcar_pagado, name='marcar_pagado'),
]
