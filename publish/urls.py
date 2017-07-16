from django.conf.urls import url

from . import views
from . import enterprise

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lead$', views.new_lead, name='lead'),
    url(r'^list$', views.get_leads, name='list_leads'),
    url(r'^test$', views.tests_leads, name='tests'),
    url(r'^enterprise', enterprise.get_enterprise, name='list_enterprices')
]