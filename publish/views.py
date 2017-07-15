from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_last_lead(request):

    return JsonResponse({})

def get_photo(request):
    return

def new_lead(request):
    print(repr(request))
    json_data = request.POST.keys()
    print(json_data)
    return True