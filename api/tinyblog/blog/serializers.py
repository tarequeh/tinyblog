from rest_framework import serializers

from tinyblog.blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
