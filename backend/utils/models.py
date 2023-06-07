from django.db import models


class ESOBase(models.Model):

    slug = models.SlugField()

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        abstract = True


class Tag(ESOBase):

    name = models.CharField(max_length=100)


class Category(ESOBase):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'


class ArchiveBase(ESOBase):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    published = models.BooleanField(default=False)
    publication_datetime = models.DateTimeField()
    embargo_datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        abstract = True

