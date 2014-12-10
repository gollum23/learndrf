# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns, include
# Import format suffix
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail, UserList, UserDetail

urlpatterns = patterns(
    '',
    url(r'^$', SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

# Add format suffix to urls
urlpatterns = format_suffix_patterns(urlpatterns)