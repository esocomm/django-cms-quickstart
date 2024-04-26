# Generated by Django 3.2 on 2023-06-09 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('publication_datetime', models.DateTimeField()),
                ('embargo_datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credit', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.category')),
                ('tags', models.ManyToManyField(to='utils.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('publication_datetime', models.DateTimeField()),
                ('embargo_datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credit', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.category')),
                ('tags', models.ManyToManyField(to='utils.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoInAFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('publication_datetime', models.DateTimeField()),
                ('embargo_datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credit', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.category')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esomedia.videoformat')),
                ('poster', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videoinaformat_poster', to=settings.FILER_IMAGE_MODEL)),
                ('tags', models.ManyToManyField(to='utils.Tag')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esomedia.video')),
                ('video_file', filer.fields.file.FilerFileField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videoinaformat_video', to='filer.file')),
            ],
            options={
                'verbose_name_plural': 'Videos in a format',
            },
        ),
        migrations.CreateModel(
            name='ImageInAFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='esomedia.imageformat')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esomedia.image')),
                ('image_file', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Images in a format',
            },
        ),
    ]