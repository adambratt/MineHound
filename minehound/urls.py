from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'server.views.home'),
    url(r'^server/create/$', 'server.views.create'),
    url(r'^server/view/(?P<server_id>\w+)/$', 'server.views.view'),
    
    url(r'^dashboard/$', 'member.views.dashboard'),
    
    url(r'^accounts/', include('registration.backends.default.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
)
