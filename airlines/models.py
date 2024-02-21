import uuid
from django.db import models

class Airlines(models.Model):
    uuid = models.UUIDField(
        'Уникальный идентификатор объекта',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    icao_code = models.CharField('ИКАО код авиакомпании')
    iata_code = models.CharField('ИАТА код авиакомпании')
    airline_name = models.CharField('Названиеавиакомпании')
    extra_info = models.TextField('Дополнительная информация в свободной форме', null=True)

    def __str__(self):
        return f'{self.name} {self.uuid}'