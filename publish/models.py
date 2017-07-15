from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    email = models.EmailField()
    location = models.CharField(max_length=200)
    enterprise =  models.CharField(max_length=200)
    role =  models.CharField(max_length=200)
    address =  models.CharField(max_length=200)
    phone = models.IntegerField()
    tags = models.CharField(max_length=200)
    photo = models.ImageField()
    facebook_link = models.URLField()
    linkedin_link = models.URLField()
    instagram_link = models.URLField()
