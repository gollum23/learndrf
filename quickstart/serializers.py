# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
# Importar de modelos de usuario y grupo
from django.contrib. auth.models import User, Group
# Importar serializadores
from rest_framework import serializers


# Clase que hereda de HyperlinkedModelSerializer para serializar el modelo User
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# Clase que hereda de HyperlinkedModelSerializer para serializar el modelo Group
class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')