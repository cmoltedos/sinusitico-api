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
    user_id = request.META['X_LEADIN_USER']
    leadstatus = LeadStatus()
    leadstatus.lead = lead
    leadstatus.publisher = User.objects.get(id=user_id)
    leadstatus.save()
    return HttpResponse()

def get_leads(request):
    if len(LeadStatus.objects.all()) <= 0:
        fake.charge_leads()
        fake.charge_leadstatus()
    results = list()
    for leadstatus in LeadStatus.objects.all():
        if leadstatus.is_taked():
            continue
        lead = leadstatus.lead
        day_pass = now() - lead.pub_date
        result = model_to_dict(lead)
        result['location'] = lead.location_parser()
        is_premium = len([1 for value in result.values() if value != None]) >= 9
        result.update({'days_pass': day_pass.days, 'is_premium': is_premium})
        result.update(model_to_dict(leadstatus))
        results.append(result)
    return JsonResponse({'list': results}, safe=False)

@csrf_exempt
def login(request):
    if len(User.objects.all()) <= 0:
        fake.charge_users()
    json_data = json.loads(request.body)
    user = User.objects.get(username=json_data['username'])
    return JsonResponse(model_to_dict(user), safe=False)

def get_leads_by_user(request):
    user_id = request.GET['userid']
    user = User.objects.get(id=user_id)
    results = list()
    for leadstatus in LeadStatus.objects.all():
        if leadstatus.consumer_id != user.id:
            continue
        lead = leadstatus.lead
        day_pass = now() - lead.pub_date
        result = model_to_dict(lead)
        result['location'] = lead.location_parser()
        is_premium = len([1 for value in result.values() if value != None]) >= 9
        result.update({'days_pass': day_pass.days, 'is_premium': is_premium})
        result.update(model_to_dict(leadstatus))
        results.append(result)
    return JsonResponse({'list': results}, safe=False)

@csrf_exempt
def change_leadstatus(request):
    user_id = request.GET['userid']
    user = User.objects.get(id=user_id)
    json_data = json.loads(request.body)
    lead = Lead.objects.get(id=json_data['id'])
    leadstatus = LeadStatus.objects.get(lead=lead)
    leadstatus.consumer = user
    leadstatus.accepted = json_data['accepted'] if json_data['accepted'] else False
    leadstatus.in_progress = json_data['in_progress'] if json_data['in_progress'] else False
    leadstatus.close_lost = json_data['close_lost'] if json_data['close_lost'] else False
    leadstatus.close_won = json_data['close_won'] if json_data['close_won'] else False
    leadstatus.save()
    return JsonResponse({}, safe=False)