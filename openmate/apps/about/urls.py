# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView, RedirectView
from contact_form.views import contact_form

urlpatterns = patterns('',

	url(r'^fiubar/$', TemplateView.as_view(template_name='about/fiubar.html'),
		name='about-fiubar'),

	url(r'^faq/$', TemplateView.as_view(template_name='about/faq.html'),
		name='about-faq'),

	url(r'^bugs/$', contact_form,
		{ 'template_name': 'about/bugs_form.html',
		  'success_url' : '/about/bugs/sent/' },
		name='about-bugs'),

	url(r'^bugs/sent/$', TemplateView.as_view(template_name='about/bugs_form_sent.html'),
		name='about-bugs_sent'),

	url(r'^$', RedirectView.as_view(url='/about/fiubar/')),

	url(r'^contact/$', contact_form,
		{ 'template_name': 'about/contact_form.html',
		  'success_url' : '/about/contact/sent/' },
		name='about-contact'),

	url(r'^contact/sent/$', TemplateView.as_view(template_name='about/contact_form_sent.html'),
		name='about-contact_sent'),

	#url(r'^ideas/$', 'ideas',
	#	name='about-ideas'),

	#url(r'^brainstorm/$', TemplateView.as_view(template_name='about/brainstorm.html'),
	#	name='about-brainstorm'),

	#url(r'^participate/$', 'participate_form',
	#	name='about-participate'),

)
