from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',
        'tutorBase.views.index', name='index'),

    url(r'^login/',
        'tutorBase.views.login', name='login'),

    url(r'^create/',
        'tutorBase.views.create_user', name='create_user'),

    url(r'^verify/',
        'tutorBase.views.verify', name='verify'),

    url(r'^logout/',
        'tutorBase.views.logout', name='logout'),

    url(r'^who/',
        'tutorBase.views.who', name='who'),

    url(r'^tutor/',
        'tutorBase.views.tutor', name='tutor'),

    url(r'^search/',
        'tutorBase.views.search_all', name='search'),

    url(r'^stanford/$',
        'tutorBase.views.stanford', name='stanford'),

    url(r'^stanford/(?P<school>\w+)/$',
        'tutorBase.views.stanford', name='stanford'),

    url(r'^stanford/(?P<school>\w+)/(?P<department>\w+)/$',
        'tutorBase.views.stanford', name='stanford'),

    url(r'^stanford/(?P<school>\w+)/(?P<department>\w+)/(?P<key>\d+)/$',
        'tutorBase.views.stanford', name='stanford')
)