from rest_framework import serializers
from .models import APODImage, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class APODImageSerializer(serializers.HyperlinkedModelSerializer):
    tagsLink = serializers.HyperlinkedRelatedField(
        view_name="apod-image-tags",
        read_only=True,
        many=True,
    )

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
            "tagsLink",
        ]
