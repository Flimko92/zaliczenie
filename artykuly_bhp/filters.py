import django_filters
from .models import produkty, przydzial
from django import forms

class ProduktyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    exp_date = django_filters.DateRangeFilter()
    count__gt = django_filters.NumberFilter(name='count', lookup_expr='count__gt')
    count__lt = django_filters.NumberFilter(name='count', lookup_expr='count__lt')
    class Meta:
        model = produkty
        fields = ['name', 'exp_date']

class PrzydzialFilter(django_filters.FilterSet):
    what = django_filters.ModelMultipleChoiceFilter(queryset=produkty.objects.all(), widget=forms.CheckboxSelectMultiple)
    when = django_filters.DateRangeFilter()
    class Meta:
        model = przydzial
        fields = ['who', 'what', 'when']