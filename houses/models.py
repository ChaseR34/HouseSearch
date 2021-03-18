from django.db import models


# Create your models here.

class CraigsList(models.Model):
    title = models.TextField(null=True)
    price = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    sq_ft = models.IntegerField(null=True)
    city = models.TextField(null=True)
    date_listed = models.DateField(null=True)
    link = models.TextField()
    img = models.ImageField(null=True)