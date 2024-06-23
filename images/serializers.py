from rest_framework import serializers
from .models import APODImage

class APODImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = APODImage
        exclude = ('image_bytes',)
