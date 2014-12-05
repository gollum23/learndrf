# -*- coding: utf-8 -*-
__author__ = 'gollum23'
__date__ = '12/5/14'
from django.conf.urls import patterns, url, include
from rest_framework import routers
from .views import *

# Crear el router for defecto
router = routers.DefaultRouter()
# Registrar la vista UserViewSet a la url /users/
router.register(r'users', UserViewSet)
# Registrar la vista GroupViewSet a la url /groups/
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    # Incluir en la url base / las urls generadas por el router
    url(r'^', include(router.urls)),
    # Incluir las vistas por defecto para login y logout de la API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
