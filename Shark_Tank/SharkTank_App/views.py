from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from SharkTank_App.models import Data
from django.core import serializers
from django.db.models import Q
from SharkTank_App.filters import DataFilter
from django_filters.views import FilterView

# Create your views here.
def home(request):
    if request.method == 'GET':
        res = serializers.serialize("json", Data.objects.filter(season='1',no_in_series='1'))
        # return JsonResponse({'Details': res}, status=200)
        return HttpResponse(res)

def home1(request):
    if request.method == 'GET':
        # Selcting all rows which have not funded
        #res = serializers.serialize("json",Data.objects.filter(Q(corcoran__isnull = True)&Q(cuban__isnull = True)&Q(griener__isnull = True)&Q(herjavec__isnull = True)&Q(john__isnull = True)&Q(oleary__isnull = True)&Q(harrington__isnull = True)))
        res = serializers.serialize("json", Data.objects.filter(no_of_sharks = '0'))
        print(Data.objects.filter(no_of_sharks = '0').count())
        return HttpResponse(res)

def home2(request):
    if request.method == 'GET':
        # Selcting all rows which have not funded
        #res = serializers.serialize("json",Data.objects.filter(Q(corcoran__isnull = True)&Q(cuban__isnull = True)&Q(griener__isnull = True)&Q(herjavec__isnull = True)&Q(john__isnull = True)&Q(oleary__isnull = True)&Q(harrington__isnull = True)))
        res = serializers.serialize("json", Data.objects.filter(Q(amount__exact = '')&Q(no_of_sharks='0')))
        print(Data.objects.filter(Q(amount__exact = '')&Q(no_of_sharks='0')).count())
        return HttpResponse(res)
#Filtering operations using FilterClass Set    
def filter_opr(request):
	data= Data.objects.all()
	filter = DataFilter(request.GET, queryset = data)
	return render(request, 'search/data_filter.html', {'filter' : filter})
