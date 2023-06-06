from django.db import models
from media.models import Image, Video
from utils.models import ArchiveBase


class PressRelease(ArchiveBase):

    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=100, null=True, blank=True)

    main_text = models.TextField()
    more_information = models.TextField()
    links = models.TextField()
    contacts = models.TextField()

    images = models.ManyToMany(Image)
    videos = models.ManyToMany(Video)

