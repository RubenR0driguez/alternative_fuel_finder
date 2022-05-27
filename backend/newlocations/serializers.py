from rest_framework import serializers
from .models import Location


class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'bussiness_name', 'address', 'fuel_type']
