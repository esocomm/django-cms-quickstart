from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from backend.utils.models import ESOBase, ArchiveBase


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
        abstract = True


class Image(MediaBase):

    pass


class ImageInAFormat(models.Model):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    format = models.ForeignKey(ImageFormat, on_delete=models.SET_NULL, null=True)
    image_file = FilerImageField(on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Images in a format"


class Video(MediaBase):

    pass


class VideoInAFormat(MediaBase):

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    format = models.ForeignKey(VideoFormat, on_delete=models.SET_NULL, null=True)
    poster = FilerImageField(on_delete=models.SET_NULL, null=True, related_name='videoinaformat_poster')
    video_file = FilerFileField(on_delete=models.SET_NULL, null=True, related_name='videoinaformat_video')

    class Meta:
        verbose_name_plural = "Videos in a format"


