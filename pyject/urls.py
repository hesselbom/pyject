from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()


urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$', 'users.views.login', name='home'),
    url(r'^users/', include('users.urls')),
    url(r'^projects/', include('projects.urls'))
)
