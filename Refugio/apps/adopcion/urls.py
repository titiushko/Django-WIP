from django.conf.urls import url
from apps.adopcion.views import index, agregar, modificar, eliminar

urlpatterns = [
    url(r'^adopciones$', index.as_view(), name = 'index'),
    url(r'^adopciones/agregar', agregar.as_view(), name = 'agregar'),
    url(r'^adopciones/modificar/(?P<pk>\d+)/$', modificar.as_view(), name = 'modificar'),
    url(r'^adopciones/eliminar/(?P<id>\d+)/$', eliminar, name = 'eliminar'),
]
