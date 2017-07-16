from django.db import models
from django.utils.timezone import now
# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, null=True)

class Lead(models.Model):
    name = models.CharField(max_length=20, null=True)
    pub_date = models.DateTimeField(verbose_name='date published', default=now(), blank=True)
    email = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True)
    enterprise =  models.CharField(max_length=200, null=True)
    role =  models.CharField(max_length=200, null=True)
    address =  models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    tags = models.CharField(max_length=200, null=True)
    facebook_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    oportunity = models.TextField(null=True)

