from django.urls import path
from .views import APODImageDetailsAPIView, APODImageList, APODImageRandom

urlpatterns = [
    path("", APODImageList.as_view(), name="apod-image-list"),
    path("random/", APODImageRandom.as_view(), name="apod-image-random"),
    path("<str:date>/", APODImageDetailsAPIView.as_view(), name="apod-image-detail"),
]
