from django.db import models

class Post(models.Model):
    title_text = models.CharField(max_length=200)
    content_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
