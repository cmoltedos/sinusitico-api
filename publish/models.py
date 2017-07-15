from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    pub_date = models.DateTimeField(verbose_name='date published', auto_now=True)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200)
    enterprise =  models.CharField(max_length=200)
    role =  models.CharField(max_length=200)
    address =  models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)
    tags = models.CharField(max_length=200)
    photo = models.ImageField() # Install Pillow (pip install Pillow)
    facebook_link = models.URLField(unique=True)
    linkedin_link = models.URLField(unique=True)
    instagram_link = models.URLField(unique=True)
    oportunity = models.TextField()
