from django.views.generic import ListView, DetailView
from django.urls import path

from . import views
urlpatterns = [
    path('test', views.home)

]
