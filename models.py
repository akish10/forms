from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Article(models.Model):

    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)

    class Meta:

        db_table='article'