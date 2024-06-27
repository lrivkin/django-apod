from rest_framework import serializers
from .models import APODImage, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class APODImageSerializer(serializers.HyperlinkedModelSerializer):
    # NOTE: would probably prefer for this to be a hyperlinked field but ran out of time to actually get that working with the tags view
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
