# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from openmate.core import global_urls
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = patterns('',
	# temporary...
	url(r'^home/', RedirectView.as_view(url='/noticias/')),
	url(r'^$', RedirectView.as_view(url='/noticias/')),
)

if getattr(settings, 'DEBUG', True):

	urlpatterns += patterns('',

		url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		  { 'document_root': settings.STATIC_ROOT, 'show_indexes': True, },
		),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		  { 'document_root': settings.MEDIA_ROOT, 'show_indexes': True, },
		),

	)

urlpatterns += global_urls.urlpatterns
