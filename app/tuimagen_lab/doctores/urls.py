from django.urls import path
from .views import buscar_doctor

urlpatterns = [
    path('buscar_doctor/', buscar_doctor, name='buscar_doctor'),
]
