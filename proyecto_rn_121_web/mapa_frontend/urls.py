from django.urls import path
from . import views

app_name = 'mapa_frontend'
urlpatterns = [
    path('', views.Pozos_rn121ListaMapa, name='Pozos_rn121-lista-mapa')
]