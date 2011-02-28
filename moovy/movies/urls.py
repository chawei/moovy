from django.conf.urls.defaults import *

urlpatterns = patterns('moovy.movies.views',
    (r'^$', 'index'),
)