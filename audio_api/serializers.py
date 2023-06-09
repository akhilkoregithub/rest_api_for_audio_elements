from rest_framework import serializers
from .models import AudioElement


class AudioElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioElement
        fields = '__all__'
