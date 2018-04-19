from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contas),
     url(r'^busca', views.busca),
    url(r'^editar', views.editar),
    url(r'^pagar', views.pagar),
    ]
