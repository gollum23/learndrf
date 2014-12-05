# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.forms import widgets
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    # Definición de campos que son serializados y deserializados
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100
    )
    code = serializers.CharField(
        style={'type': 'textarea'}
    )
    linenos = serializers.BooleanField(
        required=False
    )
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES,
        default='python'
    )
    style = serializers.ChoiceField(
        choices=STYLE_CHOICES,
        default='friendly'
    )

    def create(self, validated_data):
        """
        Crear y regresar una nueva instancia de Snippet, luego de validar los datos
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualizar y regresar una instancia existente de Snippet, luego de validar los datos
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data('code', instance.code)
        instance.linenos = validated_data('linenos', instance.linenos)
        instance.language = validated_data('language', instance.language)
        instance.style = validated_data('style', instance.style)
        instance.save()
        return instance