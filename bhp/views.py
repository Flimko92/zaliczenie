# coding: utf-8
from django.views.generic import TemplateView, ListView, DetailView
from artykuly_bhp.models import przydzial

class HomeTemplateView (ListView):
    model = przydzial
    template_name = 'home.html'