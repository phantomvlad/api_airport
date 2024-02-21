from rest_framework import serializers

from airobjects.validators import name_validate
from .models import Airline
from airobjects.serializers import AirObjectsSerializer

class AirlinesSerializer(AirObjectsSerializer):
    airlines_name = serializers.CharField(validators=[name_validate], required=False)
    class Meta:
        model = Airline
        fields = '__all__'
