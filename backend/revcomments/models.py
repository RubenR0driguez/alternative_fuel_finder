from django.db import models

# Create your models here.


class Comments(models.Model):
    text = models.CharField(max_length=500)
    member_id = models.CharField(max_length=255)
