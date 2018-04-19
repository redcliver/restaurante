from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^novo_prod', views.novo_prod),
    url(r'^nova_refe', views.nova_refe),
    url(r'^buscar_prod', views.buscar_prod),
    url(r'^edit_prod', views.edit_prod),
    url(r'^buscar_refe', views.buscar_refe),
    url(r'^edit_refe', views.edit_refe),
    ]
