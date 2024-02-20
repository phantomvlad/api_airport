import uuid
from django.db import models

class Aircraft(models.Model):
    uuid = models.UUIDField(
        'Уникальный идентификатор объекта',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    icao_code = models.CharField('ИКАО код самолета')
    iata_code = models.CharField('ИАТА код самолета')
    aircraft_name = models.CharField('Название самолета')
    extra_info = models.TextField('Дополнительная информация в свободной форме', null=True)

    def __str__(self):
        return f'{self.name} {self.uuid}'