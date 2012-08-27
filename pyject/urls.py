from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyject.views.home', name='home'),
    # url(r'^pyject/', include('pyject.foo.urls')),
    url(r'^users/', include('users.urls'))
)
