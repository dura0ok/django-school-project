from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('', include('pages.urls')),
]
