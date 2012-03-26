from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'server.views.home'),
 
    url(r'^accounts/', include('registration.backends.default.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
)
