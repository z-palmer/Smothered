from django.db import models
import datetime as datetime


class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    date = models.DateField()
    time = models.TimeField()
    created = models.DateTimeField(auto_now_add=datetime)
    img = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
