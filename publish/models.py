from django.db import models
from django.utils.timezone import now
# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, null=True)

class User(models.Model):
    username = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=20, null=False)

class Lead(models.Model):
    name = models.CharField(max_length=20, null=True)
    pub_date = models.DateTimeField(verbose_name='date published', default=now(), blank=True)
    email = models.CharField(max_length=50, null=True)
    enterprise = models.ForeignKey(Enterprise, null=True)
    location =  models.CharField(max_length=200, null=True)
    role =  models.CharField(max_length=200, null=True)
    address =  models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    tags = models.CharField(max_length=200, null=True)
    facebook_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    oportunity = models.TextField(null=True)
    close_date = models.DateTimeField(verbose_name='date end', null=True)

    def location_parser(self):
        if not self.location:
            return self.location
        lat, lng = self.location.split()
        return {'lat': float(lat), 'lng': float(lng)}

class LeadStatus(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    close_won = models.BooleanField(default=False)
    close_lost = models.BooleanField(default=False)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher')
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consumer', null=True)

    def is_taked(self):
        return bool(self.accepted + self.in_progress + self.close_lost + self.close_won)

    def is_close(self):
        return bool(self.close_lost + self.close_won)
