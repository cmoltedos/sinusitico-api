from django.contrib import admin

# Register your models here.
from .models import Enterprise, User, Lead, LeadStatus

admin.site.register(Enterprise)
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(LeadStatus)