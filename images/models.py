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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
