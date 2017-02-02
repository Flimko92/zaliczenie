from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from lista_zadan.views import AlertListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(AlertListView.as_view()), name='home_page'),
    url(r'^artykuly_bhp/', include('artykuly_bhp.urls', namespace='artykuly_bhp')),
    url(r'^szkolenia/', include('szkolenia.urls', namespace='szkolenia')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)