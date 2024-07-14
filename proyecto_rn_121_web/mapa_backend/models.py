from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Pozos_rn121(models.Model):
    nodo = models.CharField(max_length=50, null=True)
    profundida = models.FloatField(null=True)
    fondo = models.FloatField(null=True)
    altura_max = models.FloatField(null=True)
    estado = models.CharField(max_length=50, null=True)
    pluvial = models.IntegerField(null=True)
    distrito = models.CharField(max_length=50, null=True)
    point_x = models.FloatField(null=True)
    point_y = models.FloatField(null=True)
    geom = models.PointField()

def __str__(self): return self.nodo

  