from django.conf.urls import patterns, url
from Things import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^edit_name/(?P<name_id>\d+)/$', views.edit_name, name='edit_name'),
                       url(r'^edit_name/(?P<name_id>0)/$', views.edit_name, name='add_name'),
                       url(r'^(?P<thing_id>0)/(?P<user_id>\d+)/$', views.edit_thing, name='add'),
                       url(r'^(?P<thing_id>\d+)/(?P<user_id>\d+)/$', views.edit_thing, name='edit_thing')

)
