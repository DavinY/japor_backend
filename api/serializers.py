from rest_framework import serializers
from .models import User
from .models import Lapor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LaporSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lapor
        fields = '__all__'
