# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

import requests
import logging

from rest_framework import generics, status, renderers
from rest_framework.response import Response

from .models import APODImage
from .serializers import APODImageSerializer

LOG = logging.getLogger(__name__)


class APODImageDetailsAPIView(generics.RetrieveAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer
    lookup_field = "date"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)

        except generics.Http404:
            api_url = f"https://api.nasa.gov/planetary/apod/?api_key={settings.API_KEY}"
            response = requests.get(api_url, params={"date": kwargs.get("date")})

            response.raise_for_status()

            serializer = self.serializer_class(data=response.json())
            if serializer.is_valid():
                serializer.save()  # Save the fetched data to your database
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
