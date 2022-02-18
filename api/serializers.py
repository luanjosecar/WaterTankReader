from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Tanks

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanks
        fields = '__all__'