# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')