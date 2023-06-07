from django.contrib import admin

from .models import (
    PressRelease,
)


class PressReleaseAdmin(admin.ModelAdmin):

    list_display = ('slug', 'published', 'publication_datetime')
    list_editable = ('published', )
    search_fields = ('slug', 'title', )
    list_filter = ('published', 'publication_datetime', 'category', 'tags')


admin.site.register(PressRelease, PressReleaseAdmin)

