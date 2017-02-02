# coding: utf-8
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import produkty, przydzial
from django_filters.views import FilterView

class ProduktyFilterView(FilterView):

    model = produkty

class PrzydzialFilterView(FilterView):

    model = przydzial

class ProduktyCreateView(CreateView):

    model = produkty
    fields = [
        'name', 'count', 'exp_date'
    ]

class ProduktyUpdateView(UpdateView):

    model = produkty
    fields = [
        'name', 'count', 'exp_date'
    ]

class IloscUpdateView(UpdateView):

    model = produkty
    fields = [
        'count'
    ]
    template_name = 'artykuly_bhp/ilosc_update.html'

class ProduktyDeleteView(DeleteView):
    model = produkty
    success_url = '/artykuly_bhp/product_list'


class PrzydzialCreateView(CreateView):

    model = przydzial
    fields = [
        'who', 'what'
    ]
