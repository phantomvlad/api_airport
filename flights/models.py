import uuid as uuid
from django.db import models
from aircrafts.models import Aircraft
from airlines.models import Airline
from airports.models import Airport

class Flights(models.Model):
    uuid = models.UUIDField(
        'Уникальный идентификатор объекта',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    flight_number = models.CharField('Номер рейса')
    '''
    Сделал удаление каскадом, т.к.,'''
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE,
                                related_name='flights',
                                verbose_name='Идентификатор авиакомпании')
    aircraft = models.ForeignKey(Aircraft,
                                 on_delete=models.CASCADE,
                                 related_name='flights',
                                 verbose_name='Идентификатор самолета')
    mar_1 = models.ForeignKey(Airport,
                              on_delete=models.CASCADE,
                              related_name='mar_1_flights',
                              verbose_name='Идентификатор аэропорта вылета')
    mar_2 = models.ForeignKey(Airport,
                              on_delete=models.CASCADE,
                              related_name='mar_2_flights',
                              verbose_name='Идентификатор аэропорта прилета')
    start_date = models.DateField('Дата начала действия рейса')
    end_date = models.DateField('Дата окончания действия рейса')
    time = models.TimeField('Время начала вполнения рейса')
    duration = models.TimeField('Продолжительность полета')
    extra_info = models.TextField('Дополнительная информация в свободной форме', null=True)


