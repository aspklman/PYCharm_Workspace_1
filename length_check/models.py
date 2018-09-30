from django.db import models

# Create your models here.
class Test(models.Model):
    country = models.CharField(primary_key='country',max_length=32)
    gdp = models.IntegerField()