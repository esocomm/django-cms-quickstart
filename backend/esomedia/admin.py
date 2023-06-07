from django.contrib import admin

from .models import (
    ImageFormat,
    ImageInAFormat,
    Image,
    VideoFormat,
    VideoInAFormat,
    Video,
)


class ImageFormatAdmin(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('slug', 'name')


class VideoFormatAdmin(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('slug', 'name')


class ImageInAFormatAdmin(admin.ModelAdmin):

    list_display = ('image', 'format')
    search_fields = ('image_slug', 'format__slug', 'format_name')
    list_filter = ('format', )


class VideoInAFormatAdmin(admin.ModelAdmin):

    list_display = ('video', 'format')
    search_fields = ('video_slug', 'format__slug', 'format_name')
    list_filter = ('format', )


class ImageInAFormatInline(admin.TabularInline):

    model = ImageInAFormat


class VideoInAFormatInline(admin.TabularInline):

    model = VideoInAFormat


class ImageAdmin(admin.ModelAdmin):

    list_display = ('slug', 'published', 'publication_datetime')
    list_editable = ('published', )
    search_fields = ('slug', 'title', 'description', 'credit')
    list_filter = ('published', 'publication_datetime', 'category', 'tags')
    inlines = [ImageInAFormatInline]


class VideoAdmin(admin.ModelAdmin):

    list_display = ('slug', 'published', 'publication_datetime')
    list_editable = ('published', )
    search_fields = ('slug', 'title', 'description', 'credit')
    list_filter = ('published', 'publication_datetime', 'category', 'tags')
    inlines = [VideoInAFormatInline]


admin.site.register(ImageFormat, ImageFormatAdmin)
admin.site.register(VideoFormat, VideoFormatAdmin)
admin.site.register(ImageInAFormat, ImageInAFormatAdmin)
admin.site.register(VideoInAFormat, VideoInAFormatAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)

