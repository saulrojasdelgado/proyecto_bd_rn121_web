from .models import Pozos_rn121
from .serializers import Pozos_rn121Serializador
from rest_framework import generics

# Create your views here.

class Pozos_rn121Lista(generics.ListAPIView):
    queryset = Pozos_rn121.objects.all()
    serializer_class = Pozos_rn121Serializador
    name = 'Pozos_rn121-lista'