from django.db import models

class Sku(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    subcategory = models.CharField(max_length=100)      

class Mart(models.Model):
    location = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    subcategory = models.CharField(max_length=100)