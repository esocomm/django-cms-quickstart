from cms.models.pluginmodel import CMSPlugin

from django.db import models


class Header(CMSPlugin):
    title = models.CharField(max_length=100, default='Title')

    def __str__(self):

        return f'{self.title}'
