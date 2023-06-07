from django.contrib import admin

from .models import (
    Tag,
    Category,
)


class TagAdmin(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('slug', 'name')


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('slug', 'name')


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

