from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.Serializer):
    class Meta:
        model=Qoshiqchi
        fields="__all__"
class AlbomSerializer(serializers.Serializer):
    class Meta:
        model=Albom
        fields="__all__"
class QoshiqSerializer(serializers.Serializer):
    class Meta:
        model=Qoshiq
        fields="__all__"
