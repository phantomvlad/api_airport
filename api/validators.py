import re

from rest_framework import serializers

def icao_validate(value):
    if not re.match(r'^[A-Z0-9]{4}$', value):
        raise serializers.ValidationError('The field must consist of 4 capital Latin letters or numbers.')

def iata_validate(value):
    if not re.match(r'^[A-Z0-9]{3}$', value):
        raise serializers.ValidationError('The field must consist of 3 capital Latin letters or numbers.')

def name_validate(value):
    if not re.match("^[a-zA-Z0-9]*$", value):
        raise serializers.ValidationError('The line must contain only Latin letters and numbers.')
