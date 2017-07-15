from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    email = models.EmailField()
    location = models.CharField(max_length=200)
    enterprise = 0
    role = 0
    address = 0
    phone = 0
    tags = 0
    photo = 0
    facebook_link = 0
    linkedin_link = 0
    instagram_link = 0
