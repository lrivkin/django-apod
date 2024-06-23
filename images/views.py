from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import APODImage
from .serializers import APODImageSerializer

class APODImageAPIView(generics.RetrieveAPIView):
    queryset = APODImage.objects.all()
    serializer_class = APODImageSerializer
    lookup_field = "date"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)
