from rest_framework import serializers

from airobjects.validators import name_validate
from .models import Airport
from airobjects.serializers import AirObjectsSerializer

class AirportsSerializer(AirObjectsSerializer):
    airport_name = serializers.CharField(validators=[name_validate], required=False)
    class Meta:
        model = Airport
        fields = '__all__'