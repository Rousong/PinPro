from django.contrib import admin

from .models import Image
from .models import Thumbnail


class ImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'image_data', 'is_published', 'image', 'height', 'width', )
    list_filter = ["is_published", ]
    list_per_page = 10

class ThumbnailAdmin(admin.ModelAdmin):

    list_display = ('id', 'original', 'image_data', 'size', 'height', 'width', )


admin.site.register(Image, ImageAdmin)

admin.site.register(Thumbnail, ThumbnailAdmin)
