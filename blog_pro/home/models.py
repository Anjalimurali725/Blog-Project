from django.db import models
from datetime import datetime,timedelta


# Create your models here.
class blog(models.Model):
    name=models.CharField(max_length=40)
    img=models.ImageField(upload_to='picture')
    cat=models.CharField(max_length=40)
    desc=models.TextField()
    author=models.CharField(max_length=50,default="smith")
    date=models.DateTimeField()


    def __str__(self):
       return '{}'.format(self.name)
class latest(models.Model):
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='picture')
    cat = models.CharField(max_length=40)
    date = models.DateTimeField()
    def __str__(self):
       return '{}'.format(self.name)