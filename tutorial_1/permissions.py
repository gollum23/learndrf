# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/10/14'
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que solo permite al dueño del
    snippet editarlo
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user