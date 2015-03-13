from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(?P<article_id>[^/]+)/$', ContentDetailsEndpoint.as_view(), name='api_v2_content_details'),
)
