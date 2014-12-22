from django.conf.urls import patterns, include, url
from django.contrib import admin
import html5_appcache

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoblog.views.home', name='home'),
    # url(r'^blog/', include('Blog.urls')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
