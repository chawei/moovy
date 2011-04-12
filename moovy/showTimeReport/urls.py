# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('showTimeReport.views',
    (r'(\d{4})/(\d{4})', 'getParam'),
)
