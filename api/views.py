from rest_framework import viewsets
from . import models
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class LaporViewset(viewsets.ModelViewSet):
    queryset = models.Lapor.objects.all()
    serializer_class = serializers.LaporSerializer
