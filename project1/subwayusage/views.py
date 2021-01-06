from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View

from django.core import serializers

from .models import SubwayUsage


# Create your views here.

class HomeView(TemplateView):
    template_name = 'subwayusage/home.html'