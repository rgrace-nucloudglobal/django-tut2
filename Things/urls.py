from django.conf.urls import patterns, url
from Things import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^edit_name/(?P<name_id>\d+)/$', views.edit_name, name='edit_name'),
                       url(r'^edit_name/(?P<name_id>0)/$', views.edit_name, name='add_name'),
                       url(r'^(?P<thing_id>0)/(?P<user_id>\d+)/$', views.edit_thing, name='add'),
                       url(r'^(?P<thing_id>\d+)/(?P<user_id>\d+)/$', views.edit_thing, name='edit_thing'),
                       url(r'^colors/$', views.colors_list, name='colors'),
                       url(r'^colors/(?P<user_id>\d+)/(?P<color_id>\d+)$', views.edit_color, name='edit_color'),
                       url(r'^colors/(?P<user_id>\d+)/(?P<color_id>0)$', views.edit_color, name='add_color')

)
