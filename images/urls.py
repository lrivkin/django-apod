from django.urls import path
from .views import APODImageDetailsAPIView

urlpatterns = [
    path("<str:date>/", APODImageDetailsAPIView.as_view(), name="apod-image-detail"),
]
