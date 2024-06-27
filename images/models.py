from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


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
    tags = models.ManyToManyField(Tag, related_name="images", blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
