# from django.conf.urls.i18n import url, patterns
from User import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/$', views.Login, name='login'),
                       url(r'^logout/$', views.Logout, name='logout')
                       )