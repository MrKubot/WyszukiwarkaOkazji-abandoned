from django.db import models


class DaneProduktu(models.Model):
    nazwa = models.CharField(max_length=150)
    URL_OLX = models.URLField()
    URL_CENEO = models.URLField()
    URL_VINTED = models.URLField()
    SCD = models.IntegerField()
 