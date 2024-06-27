from django.conf import settings

import requests

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .mixins import APODImageAPIMixin

from .models import APODImage, Tag
from .serializers import (
    APODImageSerializer,
    TagSerializer,
)


class APODImageList(generics.ListAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class APODImageRandom(APODImageAPIMixin, generics.GenericAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer

    def get(self, request, *args, **kwargs):
        response_data = self.fetch_apod_from_api({"count": 1})
        if not response_data:
            return Response(
                {"error": "API request failed"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=response_data[0])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APODImageDetailsAPIView(APODImageAPIMixin, generics.RetrieveAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer
    lookup_field = "date"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)

        except generics.Http404:
            response_data = self.fetch_apod_from_api({"date": kwargs.get("date")})
            if not response_data:
                return Response(
                    {"error": "API request failed"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = self.serializer_class(data=response_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APODImageTagsView(generics.GenericAPIView):
    queryset = APODImage.objects.all()
    lookup_field = "date"
    serializer_class = TagSerializer

    def fetch_from_huggingface(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/yanekyuk/bert-keyword-extractor"
        headers = {"Authorization": f"Bearer {settings.HUGGING_FACE_API_KEY}"}
        response = requests.post(API_URL, headers=headers, json=payload)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return None

        res_json = response.json()
        print(res_json)
        return set(item["word"] for item in res_json)

    def get(self, request, *args, **kwargs):
        apod_image = self.get_object()

        # If we already have tags saved for this image, return them
        if apod_image.tags.exists():
            serialized_tags = TagSerializer(apod_image.tags, many=True)
            return Response({"tags": serialized_tags.data}, status=status.HTTP_200_OK)

        # get tags from the image explanation field using huggingface
        explanation = apod_image.explanation
        tags_data = self.fetch_from_huggingface({"inputs": explanation})
        if not tags_data:
            return Response(
                {"error": "no tags found"}, status=status.HTTP_404_NOT_FOUND
            )

        for tag_name in tags_data:
            saved_tags = []
            tag, created = Tag.objects.get_or_create(name=tag_name)
            saved_tags.append(tag)

            apod_image.tags.add(*saved_tags)

            serialized_tags = TagSerializer(saved_tags, many=True)

            return Response({"tags": serialized_tags.data}, status=status.HTTP_200_OK)

        return Response(data=None, status=status.HTTP_404_NOT_FOUND)
