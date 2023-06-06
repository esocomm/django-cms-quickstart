from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from utils.models import ESOBase, ArchiveBase


class ImageFormat(ESOBase):

    name = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


class VideoFormat(ESOBase):

    name = models.CharField(max_length=100)


class MediaBase(ArchiveBase):

    title = models.CharField(max_length=200)
    description = models.TextField()
    credit = models.TextField()

    class Meta:
        arbstract = True


class Image(MediaBase):

    image = FilerImageField()
    format = models.ForeignKey(ImageFormat, on_delete=models.SET_NULL)


class Video(MediaBase):

    poster = FilerImageField()
    video = FilerFileField()
    format = models.ForeignKey(VideoFormat, on_delete=models.SET_NULL)


