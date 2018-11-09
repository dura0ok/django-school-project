from django.views.generic import ListView, DetailView
from django.urls import path

from . import views
urlpatterns = [
    path('pages/<int:id>', views.show_page),
    path('ask', views.ask),
    path('success', views.success),
]
