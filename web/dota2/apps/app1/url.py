__author__ = 'haohan'
from django.conf.urls import patterns, include, url
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dota2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'dashboard',dashboard),
)

