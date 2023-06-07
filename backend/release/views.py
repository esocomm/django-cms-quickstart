from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import PressRelease


class PressReleaseListView(generic.ListView):

    template_name = 'release/list.html'
    context_object_name = 'press_releases_list'

    def get_queryset(self):
        return PressRelease.objects.filter(published=True, publication_date__gte=timezone.now())

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['header_image_url'] = '/media/filer_public/37/da/37da3c06-8f69-4490-b41b-8515903332c9/header-frontpage.jpg'

        return context


class PressReleaseDetailView(generic.DetailView):

    model = PressRelease
    template_name = 'release/detail.html'


