
from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views

urlpatterns = patterns('Blog.views',
    url(r'^topic/$', 'topic_list', name='topic-list'),
    url(r'^topic/(?P<id>\d+)/$', 'topic_details', name='topic-details'),
    url(r'^topic/(?P<id>\d+)/delete/$', 'topic_delete', name='topic-delete'),
)
