from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^login$', 'tutorBase.views.login', name='login'),
)
=======
    url(r'^login$',
        'tutorBase.views.login', name='login'),
    url(r'^create$',
        'tutorBase.views.create_user', name='Create User'),
)
>>>>>>> 7ab576d81c3b6f5cd42fb4a8d6b9ac7e1312b7aa
