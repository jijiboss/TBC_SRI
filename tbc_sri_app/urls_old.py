from django.conf.urls import include, url
from django.contrib import admin

#
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tbc_sri.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sritable3$', views.sritable3, name='sritable3'),
    url(r'^myLoadData02$', views.myLoadData02, name='myLoadData02'),
    url(r'^myUpdateData02/(?P<pk>[0-9]+)$', views.myUpdateData02, name='myUpdateData02'),

"""
    ================
    old code, delete
    ================

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<namae>[^0-9])/$', views.helloWorld, name='helloWorld'),
    url(r'^$', views.index, name='index'),
    url(r'^sritable$', views.sritable, name='sritable'),
    url(r'^jquery01$', views.jquery01, name='jquery01'),
    url(r'^myLoadData$', views.myLoadData, name='myLoadData'),
    url(r'^myUpdateData$', views.myUpdateData, name='myUpdateData'),
"""
]
