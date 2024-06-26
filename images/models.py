from django.db import models


class APODImage(models.Model):
    copyright = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    explanation = models.TextField()
    hdurl = models.URLField(blank=True, null=True)
    media_type = models.CharField(max_length=50)
    service_version = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    url = models.URLField()
    image_bytes = models.BinaryField(blank=True, null=True)  # New field for image bytes
