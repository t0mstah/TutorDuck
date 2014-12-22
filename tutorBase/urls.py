from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^post/login.html$',
        'tutorBase.views.login', name='login'),
)