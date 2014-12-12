# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns, include
# Import format suffix
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail, UserList, UserDetail, SnippetHighlight

urlpatterns = patterns(
    '',
    url(r'^$', 'tutorial_1.views.api_root'),
    url(r'^snippets/$', SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

# Add format suffix to urls
urlpatterns = format_suffix_patterns(urlpatterns)