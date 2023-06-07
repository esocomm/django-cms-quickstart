from django.urls import path

from .views import PressReleaseListView, PressReleaseDetailView

app_name = "release"
urlpatterns = [
    path('/', PressReleaseListView.as_view(), name='release_list'),
    path('<slug:slug>/', PressReleaseDetailView.as_view(), name='release_detail'),
]

