from django.db import models
from airobjects.models import AirObject

class Airports(AirObject):
    airport_name = models.CharField('Названиеавие аэропорта')
    latitude = models.FloatField('Широта', blank=False, null=False)
    longitude = models.FloatField('Долгота', blank=False, null=False)
    altitude = models.FloatField('Высота', blank=False, null=False)