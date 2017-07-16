from django.conf.urls import url

from . import views
from . import enterprise

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lead$', views.new_lead, name='lead'),
    url(r'^list$', views.get_leads, name='list_leads'),
    url(r'^enterprise', enterprise.get_enterprise, name='list_enterprices'),
    url(r'^login', views.login, name='login'),
    url(r'^list_user', views.get_leads_by_user, name='list_by_user'),
    url(r'^lead_update', views.change_leadstatus, name='change_leadstatus'),

]