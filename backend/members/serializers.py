from rest_framework import serializers
from .models import Members


class membersserializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'first_name', 'last_name', 'email_address']
