from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # url(r'^', include('quickstart.urls')),
    url(r'^tutorial-1/', include('tutorial_1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
