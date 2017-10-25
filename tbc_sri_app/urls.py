from django.conf.urls import include, url
from django.contrib import admin

#
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tbc_sri.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<namae>[^0-9])/$', views.helloWorld, name='helloWorld'),
    url(r'^$', views.index, name='index'),
    url(r'^sritable$', views.sritable, name='sritable'),

]
