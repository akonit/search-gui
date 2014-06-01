from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    news_text = models.TextField(blank=True)
    data_type = models.TextField(blank=True)
    json = models.TextField(unique=True, blank=True)
    class Meta:
        db_table = 'news'