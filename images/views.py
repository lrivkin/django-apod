from django.conf import settings

import requests

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .mixins import APODImageAPIMixin

from .models import APODImage
from .serializers import APODImageSerializer


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
