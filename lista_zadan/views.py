# coding: utf-8
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import alert

class AlertListView(ListView):

    model = alert
    template_name = 'home.html'