from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image.png$', views.image_generator, name='image_generator'),
]

