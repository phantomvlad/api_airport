from django.db import models
from airobjects.models import AirObject

class Airport(AirObject):
    airport_name = models.CharField('Названиеавие аэропорта')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    altitude = models.FloatField('Высота')