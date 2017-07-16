from publish.models import Enterprise
from django.forms import model_to_dict
from django.http import JsonResponse

def set_dummy_enteprise():
    enterprice = Enterprise()
    enterprice.name = 'Carossi'
    enterprice.category = 'Alimentos'
    enterprice.save()
    enterprice = Enterprise()
    enterprice.name = 'Calaf'
    enterprice.category = 'Alimentos'
    enterprice.save()
    enterprice = Enterprise()
    enterprice.name = 'Falafela'
    enterprice.category = 'Retail'
    enterprice.save()
    enterprice = Enterprise()
    enterprice.name = 'Ropley'
    enterprice.category = 'Retail'
    enterprice.save()
    enterprice = Enterprise()
    enterprice.name = 'Almacenes Roma'
    enterprice.category = 'Retail'
    enterprice.save()
    return True

def get_enterprise(request):
    if len(Enterprise.objects.all()) <= 0:
        set_dummy_enteprise()
    results = list()
    for lead in Enterprise.objects.all():
        result = model_to_dict(lead)
        results.append(result)
    return JsonResponse({'list': results}, safe=False)