from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^login/$', 'login'),
    url(r'^dash/$', 'dash'),
    url(r'^validate/$', 'validate')
)