from rest_framework import serializers
from core import models


class Image(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
