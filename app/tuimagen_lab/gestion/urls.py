from django.urls import path
from . import views

urlpatterns = [
    path('crear_trabajo/', views.crear_trabajo, name='crear_trabajo'),
    path('', views.listar_trabajos_pendientes, name='listar_trabajos_pendientes'),
    path('terminados/', views.listar_trabajos_terminiados, name='listar_trabajos_terminiados'),
    path('detalle_trabajo', views.detalle_trabajo, name='detalle_trabajo'),
]
