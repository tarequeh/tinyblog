from django.conf.urls import patterns, include, url
from django.contrib import admin

from tinyblog.blog.endpoints import ArticleEndpoint, ArticlesEndpoint


# django admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# API URLs
urlpatterns += patterns('',
    url(r'^api/article/$', ArticlesEndpoint.as_view(), name='api_articles'),
    url(r'^api/article/(?P<article_id>[^/]+)/$', ArticleEndpoint.as_view(), name='api_article'),
)
