from django.contrib import admin
from django.urls import path, include

from .views import home, detail, new, create, postcreate, delete, update

urlpatterns = [
    path('', home, name='home'),


    path('new/', new, name='new'),
    path('detail/<int:blog_id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('postcreate/', postcreate, name='postcreate'),
    path('update/<int:blog_id>/', update, name='update'),
    path('delete/<int:blog_id>/', delete, name='delete'),
]