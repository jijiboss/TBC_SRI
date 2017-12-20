from django.conf.urls import include, url
from django.contrib import admin

#
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^base_generic$', views.baseGeneric, name='baseGeneric'),
    url(r'^sritable3$', views.sritable3, name='sritable3'),
    url(r'^myLoadData02$', views.myLoadData02, name='myLoadData02'),
    url(r'^myUpdateData02/(?P<pk>[0-9]+)$', views.myUpdateData02, name='myUpdateData02'),
]
