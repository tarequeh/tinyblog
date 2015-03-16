from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title
