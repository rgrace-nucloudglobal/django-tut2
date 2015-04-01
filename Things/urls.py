from django.conf.urls import patterns, url
from Things import views

urlpatterns = patterns('',
                       # root - default/fallback flow
                       url(r'^$', views.index, name='index'),
#                        url(r'^$', views.IndexView.as_view(), name='index'),
                       # single item root - detail flow
                       url(r'^edit_name/(?P<name_id>\d+)/$', views.edit_name, name='edit_name'),
                       url(r'^edit_name/(?P<name_id>0)/$', views.edit_name, name='add_name'),
                       url(r'^(?P<thing_id>\d+)/$', views.edit_description, name='edit_description')
                       
#                        url(r'^(?P<thing_id>\d+)/$', views.detail, name='detail'),
#                        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail')
                       # ,
                       # single item action root - user things save form submit
                       # flow
                       #                        url(r'^(?P<thing_id>|d+)/',
                       # views.Selection.as_view(), name='selection')
#                        url(r'^(?P<thing_id>\d+)/save', views.save, name='save')
)
