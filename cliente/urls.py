from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cliente1),
    url(r'^busca', views.busca),
    url(r'^editar', views.editar),
    ]
