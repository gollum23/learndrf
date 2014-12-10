# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns
# Import format suffix
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail

urlpatterns = patterns(
    '',
    url(r'^$', SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', SnippetDetail.as_view())
)

# Add format suffix to urls
urlpatterns = format_suffix_patterns(urlpatterns)