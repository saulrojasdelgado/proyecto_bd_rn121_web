from django.shortcuts import render

# Create your views here.
def Pozos_rn121ListaMapa(request):
    return render(request, 'mapa_frontend/pozos_base.html')