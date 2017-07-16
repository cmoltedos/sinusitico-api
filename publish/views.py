import datetime
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import now
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from publish.models import Lead, Enterprise, User, LeadStatus
from publish import charge_fake_data as fake


def index(request):
    return HttpResponse("Hello, world. You're at the Leadin index.")

@csrf_exempt
def new_lead(request):
    json_data = json.loads(request.body)
    lead = Lead()
    lead.name = json_data.get('nombre', None)
    lead.address = json_data.get('direccion', None)
    lead.email = json_data.get('email', None)
    lead.phone = json_data.get('telefono', None)
    lead.address = json_data.get('direccion', None)
    lead.role = json_data.get('cargo', None)
    lead.oportunity = json_data.get('comentarios', None)
    enterprise = json_data.get('empresa', None)
    if enterprise:
        lead.enterprise = Enterprise.objects.get(id=enterprise['id'])
    lead.save()
    return HttpResponse()

def get_leads(request):
    results = list()
    for lead in Lead.objects.all():
        day_pass = now() - lead.pub_date
        result = model_to_dict(lead)
        is_premium = len([1 for value in result.values() if value != None]) >= 9
        result.update({'days_pass': day_pass.days, 'is_premium': is_premium})
        results.append(result)
    return JsonResponse({'list': results}, safe=False)

def tests_leads(request):
    results = list()
    for lead in Lead.objects.all():
        day_pass = now() - lead.pub_date
        result = model_to_dict(lead)
        is_premium = len([1 for value in result.values() if value == None]) == 5
        print(is_premium)
        result.update({'days_pass': day_pass.days, 'is_premium': is_premium})
        results.append(result)
    return JsonResponse(results, safe=False)

@csrf_exempt
def login(request):
    json_data = json.loads(request.body)
    user = User.objects.get(name=json_data['username'])
    return JsonResponse(model_to_dict(user), safe=False)

def charge_data(request):
    # fake.charge_users()
    fake.charge_leads()
    return HttpResponse("Data upload")