from publish.models import Enterprise
from django.forms import model_to_dict
from django.http import JsonResponse
from publish import charge_fake_data

def get_enterprise(request):
    if len(Enterprise.objects.all()) <= 0:
        charge_fake_data.charge_enterprise()
    results = list()
    for lead in Enterprise.objects.all():
        result = model_to_dict(lead)
        results.append(result)
    return JsonResponse({'list': results}, safe=False)