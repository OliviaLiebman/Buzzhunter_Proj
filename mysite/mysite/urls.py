from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', admin.site.urls),
]