from django.test import TestCase
from django.urls import reverse
from rest_framework import status

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
