from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View

from django.core import serializers

from .models import SubwayUsage


# Create your views here.

class HomeView(TemplateView):
    template_name = 'subwayusage/home.html'

class SearchView(View):
    def get(self, request, key):
        from .subwayusage_repository import UsageRepository
        import json

        repository = UsageRepository()
        searched_usage = repository.select_subwayusage_by_name(key)
        json_usage = json.dumps(searched_usage, ensure_ascii=False)
        return HttpResponse(json_usage, content_type='application/json')
    
class DetailView(View):
    def get(self, request, pk):

        from .subwayusage_repository import UsageRepository
        import json

        usage = UsageRepository().select_subwayusage_by_station(pk)

        

        json_usage = json.dumps(usage, ensure_ascii=False)
        return HttpResponse(json_usage, content_type='application/json')





