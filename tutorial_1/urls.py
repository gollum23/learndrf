# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns
# Import format suffix
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    'tutorial_1.views',
    url(r'^$', 'snippet_list'),
    url(r'^(?P<pk>[0-9]+)/$', 'snippet_detail')
)

# Add format suffix to urls
urlpatterns = format_suffix_patterns(urlpatterns)