from django.db import models
from django.utils.encoding import force_text


class Article(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return force_text(self.title).encode('utf-8')

    def __unicode__(self):
        return u'%s' % self.title
