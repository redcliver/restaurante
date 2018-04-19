from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contas),
     url(r'^busca', views.busca),
    url(r'^editar1', views.editar1),
    url(r'^pagar', views.pagar),
    ]
