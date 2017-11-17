from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns # for the rest framework
from tbc_sri_app import views #for the rest framework

#
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tbc_sri.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)), #I will get name space warning if I have this in additon to the Project URLS.py
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<namae>[^0-9])/$', views.helloWorld, name='helloWorld'),
    url(r'^$', views.index, name='index'),
    url(r'^sritable$', views.sritable, name='sritable'),
    url(r'^sritable3$', views.sritable3, name='sritable3'),
    url(r'^jquery01$', views.jquery01, name='jquery01'),
    url(r'^myLoadData$', views.myLoadData, name='myLoadData'),
    url(r'^myUpdateData$', views.myUpdateData, name='myUpdateData'),
    url(r'^myRest$', views.myRest.as_view(), name='myRest'),
    url(r'^myPutRest$', views.myPutRest.as_view(), name='myPutRest'),
    url(r'^myPutRest/(?P<pk>[0-9]+)$', views.myPutRest.as_view(), name='myPutRest'),
#    url(r'^myRestDetail$', views.myRestDetail.as_view(), name='myRestDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
