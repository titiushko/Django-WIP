from django.conf.urls import url
from apps.mascota.views import index, agregar

urlpatterns = [
    url(r'^$', index, name = 'inicio'),
    url(r'^mascota/agregar', agregar, name = 'agregar_mascota'),
]
