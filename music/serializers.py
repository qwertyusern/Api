from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qoshiqchi
        fields="__all__"
    def validate_fayl(self,q):
        if q not in ["Mumtoz","Rep","Pop","Jazz"]:
            raise ValidationError("Bunday turdagi qoshiq mavjud emas!")
        return q
class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Albom
        fields="__all__"
    def validate_fayl(self,a):
        if len(a)<4:
            raise ValidationError("Bunday qisqa albom mavjut emas!")
        return a
class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qoshiq
        fields="__all__"
    def validate_fayl(self,q):
        if not q.endswith(".mp3"):
            raise ValidationError("Bunaqa link yoq!")
        return q

