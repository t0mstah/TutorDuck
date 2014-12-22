from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^login.html$',
        'tutorBase.views.login', name='login'),
    url(r'^create.html$',
        'tutorBase.views.create_user'),
)