from django.db import models


class Forum(models.Model):
    author = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)


class Discussion(models.Model):
    author = models.CharField(max_length=50)
    r = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    response = models.TextField(max_length=2000)


# class Image(models.Model):
#     author = models.CharField(max_length=50)
#     topic = models.CharField(max_length=100)
#     upload = models.FileField(upload_to=)