from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),   
   
    url(r'^admin/', include(admin.site.urls)),
)
