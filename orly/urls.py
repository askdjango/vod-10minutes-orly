from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cover/', include('cover.urls', namespace='cover')),
    url(r'^$', lambda r: redirect('cover:index')),
]
