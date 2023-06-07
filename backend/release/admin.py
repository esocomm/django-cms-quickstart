from django.contrib import admin

from .models import (
    PressRelease,
    ImageVisual,
    VideoVisual,
)


class ImageVisualInline(admin.TabularInline):

    model = ImageVisual


class VideoVisualInline(admin.TabularInline):

    model = VideoVisual


class PressReleaseAdmin(admin.ModelAdmin):

    list_display = ('slug', 'published', 'publication_datetime')
    list_editable = ('published', )
    search_fields = ('slug', 'title', )
    list_filter = ('published', 'publication_datetime', 'category', 'tags')
    inlines = [ImageVisualInline, VideoVisualInline]


admin.site.register(PressRelease, PressReleaseAdmin)

