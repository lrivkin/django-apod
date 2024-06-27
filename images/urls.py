from django.urls import path
from .views import (
    APODImageDetailsAPIView,
    APODImageList,
    APODImageRandom,
    APODImageTagsView,
)

urlpatterns = [
    path("", APODImageList.as_view(), name="apod-image-list"),
    path("random/", APODImageRandom.as_view(), name="apod-image-random"),
    path("<str:date>/", APODImageDetailsAPIView.as_view(), name="apod-image-detail"),
    path(
        "<str:date>/tags/",
        APODImageTagsView.as_view(),
        name="apod-image-tags",
    ),
]
