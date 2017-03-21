from django.conf.urls import url, include
from rest_framework import routers
from .views import user_interactionViewSet, page_interactionViewSet


# from .views import page_interactionViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'api/table1', user_interactionViewSet)
router.register(r'api/table2', page_interactionViewSet)

urlpatterns = [
    url(r'^api/index/1', views.ApiIndexView1.as_view()),
    url(r'^api/index/2', views.ApiIndexView2.as_view()),
    url(r'^api/index/3', views.ApiIndexView3.as_view()),

    url(r'^api/', include(router.urls)),
   # url(r'^api$', include(router.urls)), changed to above line

    url(r'^website/', views.website, name='website'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^index/', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^buzzlove/', views.buzzlove, name='buzzLove'),
    url(r'^creative/', views.creative, name='creative'),
    url(r'^index_all/', views.index_all, name='index_all'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^heatmap_website/', views.heatmap_website, name='heatmap_website'),

]
