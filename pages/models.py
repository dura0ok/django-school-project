from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Page(models.Model):
    name = models.CharField(max_length=250)
    body = RichTextUploadingField()


class Menu(models.Model):
    name = models.CharField(max_length=250)
    href = models.CharField(max_length=250)
    sort = models.IntegerField()

