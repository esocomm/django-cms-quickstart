from django.urls import path

from .views import MediaListView, ImageDetailView, VideoDetailView


app_name = "backend.esomedia"
urlpatterns = [
    path('', MediaListView.as_view(), name='esomedia_list'),
    path('image/<slug:slug>/', ImageDetailView.as_view(), name='esomedia_image_detail'),
    path('video/<slug:slug>/', VideoDetailView.as_view(), name='esomedia_video_detail'),
]

