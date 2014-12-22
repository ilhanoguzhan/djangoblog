from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^publish/(?P<post_id>\d+)/$', views.publish, name='publish'),
    url(r'^unpublish/(?P<post_id>\d+)/$', views.unpublish, name='unpublish'),
    url(r'^create', views.create, name='create'),
)
