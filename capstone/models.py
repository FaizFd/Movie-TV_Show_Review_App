from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    title1 = models.TextField(default=None)
    title2 = models.TextField(default=None)
    description = models.TextField(default=None)
    cast = models.TextField(default=None)
    price = models.FloatField(max_length=10)
    category = models.CharField(max_length=64)
    categorys = models.CharField(max_length=64, null=True)
    categoryss = models.CharField(max_length=64, null=True)
    link = models.CharField(max_length=500,default=None,blank=True,null=True)
    links = models.CharField(max_length=500,default=None,blank=True,null=True)
    trailer = models.CharField(max_length=500,default=None,blank=True,null=True)
    img = models.CharField(max_length=500,default=None,blank=True,null=True)
    imgg = models.CharField(max_length=500,default=None,blank=True,null=True)
    time = models.CharField(max_length=64)


class Comment(models.Model):
    user = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()

class Cart(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()


class Alllisting(models.Model):
    listingid = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField(default=None)
    link = models.CharField(max_length=64,default=None,blank=True,null=True)

