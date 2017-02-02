# coding: utf-8
from django.conf.urls import url
from views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^instruction_list/$', login_required(InstructionListView.as_view()), name='instruction_list'),
    url(r'^instruction_list/add/$', login_required(InstructionCreateView.as_view()), name='instruction_add'),
    url(r'^documentation/add/$', login_required(DocumentationCreateView.as_view()), name='documentation_add'),
    url(r'instruction_list/update/(?P<pk>\d+)/$', InstructionUpdateView.as_view(), name='instruction_update'),
    url(r'instruction_list/delete/(?P<pk>\d+)/$', InstructionDeleteView.as_view(), name='instruction_delete'),
    url(r'instruction_list/(?P<pk>\d+)/$', InstructionDetailView.as_view(), name='instruction_detail'),
]