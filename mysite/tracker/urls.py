from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^$', views.buzzlove, name='buzzLove'),
    url(r'^$', views.creative, name='creative'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index_all, name='index_all'),
    url(r'^$', views.index_branding, name='index_branding'),
    url(r'^$', views.index_buzzLove, name='index_buzzLove'),
    url(r'^$', views.index_confidential, name='index_confidential'),
    url(r'^$', views.index_web, name='index_web'),
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^$', views.website, name='website'),
]