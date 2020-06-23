from rest_framework import serializers
from .models import ITSP

class ITSPSerializer(serializers.ModelSerializer):
    class Meta:
        model=ITSP
        fields='__all__'
