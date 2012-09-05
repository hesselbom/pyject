from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'home'),
    url(r'^(?P<project_id>\d+)', 'project'),
)
