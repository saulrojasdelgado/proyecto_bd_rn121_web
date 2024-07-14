from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Pozos_rn121

pozos_rn121_mapping = {
    'nodo': 'nodo',
    'profundida': 'profundida',
    'fondo': 'fondo',
    'altura_max': 'altura_max',
    'estado': 'estado',
    'pluvial': 'pluvial',
    'distrito': 'distrito',
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'geom': 'POINT',
}   
pozos_geojson = Path(__file__).resolve().parent / 'datos' / 'pozos.geojson'

def run(verbose=True):
    lm = LayerMapping(Pozos_rn121, pozos_geojson, pozos_rn121_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)