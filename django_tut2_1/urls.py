from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_tut2_1 import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^Things/', include('Things.urls', namespace='Things')),
                       url(r'^user/', include('User.urls', namespace='user')),
                       
                       url(r'^admin/', include(admin.site.urls))
                       )
