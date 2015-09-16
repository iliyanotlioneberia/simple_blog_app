from django.db import models


class BlogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    date = models.DateTimeField()

