from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.caixa),
    url(r'^fechar', views.fechar),
    url(r'^retirada', views.retirada),
    url(r'^inf_geral', views.inf_geral),
    ]
