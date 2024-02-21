from rest_framework import serializers

from airobjects.serializers import AirObjectsSerializer
from airobjects.validators import name_validate
from .models import Aircraft

class AircraftSerializer(AirObjectsSerializer):
    airlines_name = serializers.CharField(validators=[name_validate], required=False)
    class Meta:
        model = Aircraft
        fields = '__all__'
