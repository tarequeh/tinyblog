from django.contrib import admin
from tinyblog.blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
