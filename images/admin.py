from django.contrib import admin
from .models import APODImage
class APODImageAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "created_at")

admin.site.register(APODImage, APODImageAdmin)
