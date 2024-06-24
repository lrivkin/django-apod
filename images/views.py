from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import APODImage
from .serializers import APODImageSerializer

# LOG = logger.getLogger(__name__)
class APODImageAPIView(generics.RetrieveAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer
    lookup_field = "date"
