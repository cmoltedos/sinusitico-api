from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from publish.models import Lead


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_last_lead(request):

    return JsonResponse({})

def get_photo(request):
    return

@csrf_exempt
def new_lead(request):
    json_data = json.loads(request.body)
    lead = Lead()
    lead.name = json_data.get('nombre', '')
    lead.address = json_data.get('direccion', '')
    lead.email = json_data.get('email', '')
    lead.phone = json_data.get('telefono', '')
    lead.address = json_data.get('direccion', '')
    lead.role = json_data.get('cargo', '')
    lead.oportunity = json_data.get('comentarios', '')
    lead.enterprise = json_data.get('empresa', '')
    lead.save()
    return HttpResponse()

def get_leads(request):
    results = dict()

    return JsonResponse(results)