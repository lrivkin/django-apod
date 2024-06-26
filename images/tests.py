from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import Mock, patch

from rest_framework.test import APIClient

from .models import APODImage


class APODImageDetailsAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.image = APODImage.objects.create(
            date="2023-01-01",
            title="Test Image",
            explanation="Test Description",
            url="http://example.com/image.jpg",
        )

    def test_get_existing_object(self):
        url = reverse("apod-image-detail", kwargs={"date": self.image.date})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Image")

    @patch("images.mixins.requests.get")
    def test_fetch_new_object(self, mock_get):
        mock_response_data = {
            "copyright": None,
            "date": "2024-01-01",
            "explanation": "Some test explanation",
            "hdurl": "https://apod.nasa.gov/apod/image/1310/example.jpg",
            "media_type": "image",
            "service_version": "v1",
            "title": "The Great Astronomy thing",
            "url": "https://apod.nasa.gov/apod/image/1310/example.jpg",
        }
        mock_get.return_value.json.return_value = mock_response_data
        mock_get.return_value.status_code = 200

        url = reverse("apod-image-detail", kwargs={"date": "2024-01-01"})
        response = self.client.get(url)

        mock_get.assert_called_once_with(
            "https://api.nasa.gov/planetary/apod/",
            params={
                "date": "2024-01-01",
                "api_key": "DEMO_KEY",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
