# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns

urlpatterns = patterns(
    'tutorial_1.views',
    url(r'^$', 'snippet_list'),
    url(r'^(?P<pk>[0-9]+)/$', 'snippet_detail')
)