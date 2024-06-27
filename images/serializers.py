from rest_framework import serializers
from .models import APODImage, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class APODImageSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = APODImage
        fields = [
            "copyright",
            "date",
            "explanation",
            "media_type",
            "title",
            "url",
            "hdurl",
            "tags",
        ]
