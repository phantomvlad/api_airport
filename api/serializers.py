from rest_framework import serializers
from .validators import icao_validate, iata_validate, name_validate

# Общий сериалайзер сделан для масштабирования различных объектов (добавление разичных полей в модели)
class AirObjectsSerializer(serializers.ModelSerializer):
    icao_code = serializers.CharField(validators=[icao_validate], required=True)
    iata_code = serializers.CharField(validators=[iata_validate], required=True)
    extra_info = serializers.CharField(allow_blank=True, allow_null=False)
