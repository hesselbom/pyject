from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^login/$', 'login'),
    url(r'^dash/$', 'dash'),
    url(r'^validate/$', 'validate')
)