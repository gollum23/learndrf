# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import url, patterns, include
# Import format suffix
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from .views import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = patterns(
    '',
    url(r'^$', 'tutorial_1.views.api_root'),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

# Add format suffix to urls
urlpatterns = format_suffix_patterns(urlpatterns)