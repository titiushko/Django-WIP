from django.conf.urls import url
from apps.mascota.views import index, agregar, modificar, eliminar

urlpatterns = [
    url(r'^mascotas$', index, name = 'index'),
    url(r'^mascotas/agregar$', agregar, name = 'agregar'),
    url(r'^mascotas/modificar/(?P<id>\d+)$', modificar, name = 'modificar'),
    url(r'^mascotas/eliminar/(?P<id>\d+)$', eliminar, name = 'eliminar'),
]
