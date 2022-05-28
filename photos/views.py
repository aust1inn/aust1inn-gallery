from django.conf.urls import url
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .import views

# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/(?P<location>\w+)/', views.location_img, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)