from django.db import models

# Create your models here.


class Location(models.Model):
    bussiness_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
