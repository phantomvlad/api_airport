from rest_framework import serializers

from api.validators import name_validate
from .models import Airports
from airobjects.serializers import AirObjectsSerializer

class AirportsSerializer(AirObjectsSerializer):
    airport_name = serializers.CharField(validators=[name_validate], required=False)
    class Meta:
        model = Airports
        fields = '__all__'