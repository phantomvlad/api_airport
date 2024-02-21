from django.db import models
from airobjects.models import AirObject

class Aircraft(AirObject):
    aircraft_name = models.CharField('Название самолета', blank=False, null=False)