# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    Listado de todos los códigos snippets, o crear un nuevo snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Lee, actualiza o borra un snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer