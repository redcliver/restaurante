from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedido1),
    url(r'^abrir', views.abrir),
    url(r'^busca', views.busca2),
    ]
