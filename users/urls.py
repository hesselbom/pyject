from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^dash/$', 'dash'),
    url(r'^validate/$', 'validate')
)
