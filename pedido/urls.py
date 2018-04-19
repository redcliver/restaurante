from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedido1),
    url(r'^abrir', views.abrir),
    url(r'^busca', views.busca2),
    url(r'^add_refe', views.add_refe),
    url(r'^add_prod', views.add_prod),
    url(r'^metodo', views.metodo),
    url(r'^finalizar', views.finalizar),
    ]
