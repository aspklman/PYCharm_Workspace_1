from django.db import models

# Create your models here.
class Gdpdata(models.Model):
    country = models.CharField(primary_key=True,max_length=32)
    gdp = models.IntegerField()

    class Meta:
        db_table = 'gdpdata'