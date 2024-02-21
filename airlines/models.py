from django.db import models
from airobjects.models import AirObject
class Airlines(AirObject):
    airline_name = models.CharField('Названиеавиакомпании')