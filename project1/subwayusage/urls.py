from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SearchView, DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('search/<str:key>', SearchView.as_view(), name='search'),
    path('detail/<str:pk>', DetailView.as_view(), name='detail'),
]