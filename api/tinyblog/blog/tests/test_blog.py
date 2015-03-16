from django.contrib.auth.models import User

from django.test import TestCase
from django.test.client import Client

from django.core.urlresolvers import reverse

from tinyblog.blog.models import Article


class BlogTests(TestCase):

    def setUp(self, *args, **kwargs):
        super(BlogTests, self).setUp(*args, **kwargs)
        self.client = Client()


    def test_get_blog_article(self):
        article_1 = Article.objects.create(title='Article 1',
            content='Article 1')
        article_2 = Article.objects.create(title='Article 2',
            content='Article 2')

        response = self.client.get(reverse('api_articles'))
        self.assertEqual(response.data['count'], 2)

        response = self.client.get(reverse('api_article', args=[article_1.pk]))
        self.assertEqual(response.data['title'], 'Article 1')
