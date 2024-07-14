from django.urls import path
from . import views

urlpatterns = [
    path("Pozos_rn121/", views.Pozos_rn121Lista.as_view(), name=views.Pozos_rn121Lista.name),
]