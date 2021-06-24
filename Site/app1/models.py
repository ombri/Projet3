from django.db import models


class Stream(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    link = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
