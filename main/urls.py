from django.views.generic import ListView, DetailView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import NewsList
from . import views
urlpatterns = [
    path('', views.home),
    path('news', NewsList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
