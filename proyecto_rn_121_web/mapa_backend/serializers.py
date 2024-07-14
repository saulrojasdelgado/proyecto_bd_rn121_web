from .models import Pozos_rn121
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class Pozos_rn121Serializador(GeoFeatureModelSerializer):
    class Meta:
        model = Pozos_rn121
        geo_field = 'geom'

        fields = (
            'id',
            'nodo',
            'profundida',
            'fondo',
            'altura_max',
            'estado',
            'pluvial',
            'distrito',
            'point_x',
            'point_y'
        )
