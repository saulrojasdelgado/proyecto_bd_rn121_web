# Generated by Django 4.2.13 on 2024-07-13 16:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pozos_rn121',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodo', models.CharField(max_length=50, null=True)),
                ('profundida', models.FloatField(null=True)),
                ('fondo', models.FloatField(null=True)),
                ('altura_max', models.FloatField(null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
                ('pluvial', models.IntegerField(null=True)),
                ('distrito', models.CharField(max_length=50, null=True)),
                ('point_x', models.FloatField(null=True)),
                ('point_y', models.FloatField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
