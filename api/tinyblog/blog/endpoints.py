from collections import OrderedDict

from django.shortcuts import get_object_or_404

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from tinyblog.blog.models import Article
from tinyblog.blog.serializers import ArticleSerializer


class ArticlesEndpoint(APIView):
    """
    Endpoint to fetch a all articles
    """
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Return all blog articles
        """
        queryset = Article.objects.all()
        paginator = PageNumberPagination()
        paginator.paginate_queryset(queryset, request)

        articles_serializer = ArticleSerializer(paginator.page, many=True)
        return paginator.get_paginated_response(
            articles_serializer.data)


class ArticleEndpoint(APIView):
    """
    Endpoint to fetch a single article
    """
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, article_id):
        """
        Return a specific blog article
        """
        article = get_object_or_404(Article.objects.all(), pk=article_id)
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data)
