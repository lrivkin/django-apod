from django.contrib import admin
from .models import APODImage
class APODImageAdmin(admin.ModelAdmin):
    exclude = ('image_bytes',)

admin.site.register(APODImage, APODImageAdmin)