import uuid
from django.db import models

#Сделана отедльная родительская модель для всех моделей Air (DRY)
class AirObject(models.Model):
    uuid = models.UUIDField(
        'Уникальный идентификатор объекта',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    icao_code = models.CharField('ИКАО код авиакомпании')
    iata_code = models.CharField('ИАТА код авиакомпании')
    extra_info = models.TextField('Дополнительная информация в свободной форме', null=True)

    def __str__(self):
        return f'{self.name} {self.uuid}'

    class Meta:
        abstract = True