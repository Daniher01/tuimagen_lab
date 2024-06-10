from django.urls import path
from . import views

urlpatterns = [
    path('crear_trabajo/', views.crear_trabajo, name='crear_trabajo'),
    path('', views.listar_trabajos, name='listar_trabajos'),
    path('detalle_trabajo/<int:trabajo_id>/', views.detalle_trabajo, name='detalle_trabajo'),
]
