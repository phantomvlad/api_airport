from django.db import models
from airobjects.models import AirObject
class Airline(AirObject):
    airline_name = models.CharField('Название авиакомпании')