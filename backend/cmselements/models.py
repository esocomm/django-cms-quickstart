from cms.models.pluginmodel import CMSPlugin

from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from .consts import BACKGROUND_COLOR_CHOICES


class Header(CMSPlugin):

    title = models.CharField(max_length=100, default='Title')
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    background_image = FilerImageField(null=True, blank=False,
                                       on_delete=models.SET_NULL,
                                       related_name='image_header')

    def __str__(self):
        return f'{self.title}'


class Container(CMSPlugin):

    background = models.CharField(max_length=10, default='li',
                                  choices=BACKGROUND_COLOR_CHOICES)

    def __str__(self):
        return f'{self.get_background_display()}'


class SectionHeading(CMSPlugin):

    title = models.CharField(max_length=100, default='Title')
    include_social_media = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class SectionParagraph(CMSPlugin):

    pass 


class Video(CMSPlugin):

    title = models.CharField(max_length=100, default='Title')
    poster = FilerImageField(null=True, blank=False,
                             on_delete=models.SET_NULL,
                             related_name='video_poster')
    video = FilerFileField(null=True, blank=False,
                           on_delete=models.SET_NULL,
                           related_name='video_video')

    def __str__(self):
        return f'{self.title}'

