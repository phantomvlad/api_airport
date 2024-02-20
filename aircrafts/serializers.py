from rest_framework import serializers
from .models import Aircraft
from api.validators import icao_validate, iata_validate, name_validate

class AircraftSerializer(serializers.ModelSerializer):
    icao_code = serializers.CharField(validators=[icao_validate], required=True)
    iata_code = serializers.CharField(validators=[iata_validate], required=True)
    name = serializers.CharField(validators=[name_validate], required=False)

    class Meta:
        model = Aircraft
        fields = '__all__'
