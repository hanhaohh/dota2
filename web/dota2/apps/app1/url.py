__author__ = 'haohan'
from django.conf.urls import patterns, include, url
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dota2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dashboard/',dashboard,{'template_name':'index.html'}),
    url(r'^table/',dashboard,{'template_name':'tables.html'}),
    url(r'^chart/',dashboard,{'template_name':'charts.html'}),
    url(r'^form/',dashboard,{'template_name':'forms.html'}),
    url(r'^blank-page/',dashboard,{'template_name':'blank-page.html'}),
    url(r'^bootstrap-grid/',dashboard,{'template_name':'bootstrap-grid.html'}),
    url(r'^bootstrap-elements/',dashboard,{'template_name':'bootstrap-elements.html'}),
)

