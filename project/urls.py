__author__ = 'niels'

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='portfolio'),
    url(r'^portfolio/(?P<project_slug>.*)$', single, name='single-project'),
    url(r'^search/$', search, name='project-search'),
    url(r'^archive/$', archive, name='project-archive'),
]
