from django.db import models

# Create your models here.


#class Page

class Page(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()


class Menu(models.Model):
    name = models.CharField(max_length=250)
    href = models.CharField(max_length=250)
    sort = models.IntegerField()

