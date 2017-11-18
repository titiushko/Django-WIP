from django.conf.urls import url
from apps.general.views import index

urlpatterns = [
    url(r'^$', index, name = 'inicio')
]
