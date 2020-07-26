from django.db import models

class Posts(models.Model):
    title_text = models.CharField(max_length=200)
    content_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published')
