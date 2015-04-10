from django.conf.urls import patterns, url
from Things import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<thing_id>0)/(?P<user_id>\d+)/$', views.edit_thing, name='add'),
                       url(r'^(?P<thing_id>\d+)/(?P<user_id>\d+)/$', views.edit_thing, name='edit_thing'),
                       url(r'^colors/$', views.colors_list, name='colors'),
                       url(r'^colors/(?P<user_id>\d+)/(?P<color_id>\d+)$', views.edit_color, name='edit_color'),
                       url(r'^colors/(?P<user_id>\d+)/(?P<color_id>0)$', views.edit_color, name='add_color'),
                       url(r'^shapes/$', views.shapes_list, name='shapes'),
                       url(r'^shapes/(?P<user_id>\d+)/(?P<shape_id>\d+)$', views.edit_shape, name='edit_shape'),
                       url(r'^shapes/(?P<user_id>\d+)/(?P<shape_id>0)$', views.edit_shape, name='add_shape')

)
