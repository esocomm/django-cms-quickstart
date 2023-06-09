from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import Image, Video


class MediaListView(generic.ListView):

    template_name = 'esomedia/list.html'

    def get_queryset(self):
        from itertools import chain
        result =  list(chain(
            Image.objects.filter(published=True, publication_datetime__gte=timezone.now()),
            Video.objects.filter(published=True, publication_datetime__gte=timezone.now())
        ))
        return sorted(result, key=lambda e: e.publication_datetime, reverse=True)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['header_image_url'] = '/media/filer_public/37/da/37da3c06-8f69-4490-b41b-8515903332c9/header-frontpage.jpg'

        return context


class ImageListView(generic.ListView):

    template_name = 'esomedia/image/list.html'

    def get_queryset(self):
        return Image.objects.filter(published=True, publication_datetime__gte=timezone.now())

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['header_image_url'] = '/media/filer_public/37/da/37da3c06-8f69-4490-b41b-8515903332c9/header-frontpage.jpg'

        return context


class ImageDetailView(generic.DetailView):

    model = Image
    template_name = 'esomedia/video/detail.html'


class VideoListView(generic.ListView):

    template_name = 'esomedia/video/list.html'

    def get_queryset(self):
        return Video.objects.filter(published=True, publication_datetime__gte=timezone.now())

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['header_image_url'] = '/media/filer_public/37/da/37da3c06-8f69-4490-b41b-8515903332c9/header-frontpage.jpg'

        return context


class VideoDetailView(generic.DetailView):

    model = Video
    template_name = 'esomedia/video/detail.html'


