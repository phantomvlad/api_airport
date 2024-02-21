from rest_framework import serializers

from api.validators import name_validate
from .models import Airlines
from api.serializers import AirObjectsSerializer

class AirlinesSerializer(AirObjectsSerializer):
    airlines_name = serializers.CharField(validators=[name_validate], required=False)
    class Meta:
        model = Airlines
        fields = '__all__'
