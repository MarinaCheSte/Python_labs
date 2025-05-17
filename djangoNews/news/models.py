from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')


