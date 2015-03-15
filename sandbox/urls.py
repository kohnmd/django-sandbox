from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^uptime', include('uptime.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
