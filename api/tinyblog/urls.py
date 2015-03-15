from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

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

# Debug URLs
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^$', TemplateView.as_view(template_name='index.html'))
    )
