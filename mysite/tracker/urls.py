from django.conf.urls import url, include
from rest_framework import routers
from .views import user_interactionViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'api', user_interactionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
   # url(r'^api$', include(router.urls)), changed to above line
    url(r'^api/index/', views.ApiIndexView.as_view()),
    url(r'^website/', views.website, name='website'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^index/', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^buzzlove/', views.buzzlove, name='buzzLove'),
    url(r'^creative/', views.creative, name='creative'),
    url(r'^index_all/', views.index_all, name='index_all'),
    url(r'^index_branding/', views.index_branding, name='index_branding'),
    url(r'^index_buzzlove/', views.index_buzzLove, name='index_buzzLove'),
    url(r'^index_confidential/', views.index_confidential, name='index_confidential'),
    url(r'^index_confidential_formpage/', views.index_confidential_formpage, name='index_confidential_formpage'),
    url(r'^index_web/', views.index_web, name='index_web'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
