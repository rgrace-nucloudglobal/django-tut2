from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
#                        url(r'^$', include('Things.menu', namespace='menu')),
                       url(r'^Things/', include('Things.urls', namespace='Things')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       )
