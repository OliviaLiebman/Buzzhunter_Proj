from django.conf.urls import url, include
from rest_framework import routers
from .views import user_interactionViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'api', user_interactionViewSet)

urlpatterns = [
    url(r'^api', include(router.urls)),
    url(r'^$', views.website, name='website'),
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.blog, name='blog'),
    url(r'^$', views.buzzlove, name='buzzLove'),
    url(r'^$', views.creative, name='creative'),
    url(r'^$', views.index_all, name='index_all'),
    url(r'^$', views.index_branding, name='index_branding'),
    url(r'^$', views.index_buzzLove, name='index_buzzLove'),
    url(r'^$', views.index_confidential, name='index_confidential'),
    url(r'^$', views.index_web, name='index_web'),
]