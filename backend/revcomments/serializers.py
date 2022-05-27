from rest_framework import serializers
from .models import Comments


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text', 'member_id']
