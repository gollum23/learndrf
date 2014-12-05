# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
#from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Vista del API que permite ver o editar los usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Vista del API que permite ver o editar los grupos
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer