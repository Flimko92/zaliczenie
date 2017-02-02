# coding: utf-8
from django.conf.urls import url
from views import ProduktyFilterView, PrzydzialFilterView, ProduktyCreateView, IloscUpdateView, ProduktyUpdateView, \
    ProduktyDeleteView, PrzydzialCreateView
from filters import ProduktyFilter, PrzydzialFilter
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^product_list/$', login_required(ProduktyFilterView.as_view(filterset_class=ProduktyFilter,
        template_name='artykuly_bhp/product_list.html')), name='product_list'),
    url(r'^przydzial_list/$', login_required(PrzydzialFilterView.as_view(filterset_class=PrzydzialFilter,
        template_name='artykuly_bhp/przydzial_list.html')), name='przydzial_list'),
    url(r'^przydzial_list/add/$', login_required(PrzydzialCreateView.as_view()), name='przydzial_add'),
    url(r'^product_list/add/$', login_required(ProduktyCreateView.as_view()), name='product_add'),
    url(r'product_list/ilosc_update/(?P<pk>\d+)/$', IloscUpdateView.as_view(), name='ilosc_update'),
    url(r'product_list/update/(?P<pk>\d+)/$', ProduktyUpdateView.as_view(), name='product_update'),
    url(r'product_list/delete/(?P<pk>\d+)/$', ProduktyDeleteView.as_view(), name='product_delete'),

]