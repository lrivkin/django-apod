from django.urls import path
from .views import APODImageAPIView

urlpatterns = [
    path('image/<str:date>/', APODImageAPIView.as_view(), name='apod-image-detail'),
]
