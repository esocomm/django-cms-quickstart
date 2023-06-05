# Generated by Django 3.2 on 2023-06-05 13:41

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cmselements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='background_image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_header', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
