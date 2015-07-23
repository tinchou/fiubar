# -*- coding: utf-8 -*-
"""
Copyright (c) 2007, James Bennett
Copyright (c) 2008, OpenMate - Some changes introduced

URLConf for Django user registration.

"""

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]+ because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.

    ### Activation
    url(r'^activate/(?P<activation_key>\w+)/$',
       'registration.views.activate',
       name='registration_activate'),
       
    ### Create account
    url(r'^register/$',
       'registration.views.register',
       name='account-register'),

    url(r'^register/complete/$',
       TemplateView.as_view(template_name='registration_complete.html'),
       name='account-complete'),
   
)
