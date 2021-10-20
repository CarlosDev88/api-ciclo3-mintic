from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=150)
    img = models.CharField(max_length=200)
    price = models.FloatField(default=0) 
    company = models.CharField(max_length=150) 
    info = models.CharField(max_length=250) 
    inCart = models.BooleanField(default=False) 