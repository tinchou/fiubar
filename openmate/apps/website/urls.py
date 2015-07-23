# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='website-index'),
    url(r'^home/$', 'index', name='website-home'),
)
