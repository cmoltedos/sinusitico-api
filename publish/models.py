from django.db import models
# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=20, null=True)
    pub_date = models.DateTimeField(verbose_name='date published', auto_now=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=200, null=True)
    enterprise =  models.CharField(max_length=200, null=True)
    role =  models.CharField(max_length=200, null=True)
    address =  models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, unique=True, null=True)
    tags = models.CharField(max_length=200, null=True)
    photo = models.ImageField() # Install Pillow (pip install Pillow)
    facebook_link = models.URLField(unique=True, null=True)
    linkedin_link = models.URLField(unique=True, null=True)
    instagram_link = models.URLField(unique=True, null=True)
    oportunity = models.TextField(null=True)
