from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField()