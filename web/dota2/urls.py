from django.conf.urls import patterns, include, url
from django.contrib import admin
from dota2.apps.app1.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dota2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
)

