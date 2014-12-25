from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/',
        'tutorBase.views.login', name='login'),

    url(r'^create/',
        'tutorBase.views.create_user', name='create_user'),

    url(r'^verify/',
        'tutorBase.views.verify', name='verify'),

    url(r'^who$',
        'tutorBase.views.who', name='who'),

    url(r'^tutor/',
        'tutorBase.views.tutor', name='tutor'),

    url(r'^student$',
        'tutorBase.views.student', name='student'),
)