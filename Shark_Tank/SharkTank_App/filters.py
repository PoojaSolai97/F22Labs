from django import forms
from SharkTank_App.models import Data
import django_filters

class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Data
        fields = {
                'season' : ['iexact'],
                'no_in_series' : ['iexact'],
                'company' : ['icontains'],
                'deal' : ['iexact'],
                'amount' : ['gt' , 'lt']
        }
