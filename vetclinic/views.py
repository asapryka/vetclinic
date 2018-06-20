from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Record, Animal


def index(request):
    return render(request, 'vetclinic/index.html')

def record_list(request):
    records = Record.objects.all().order_by('visit_date')
    return render(request, 'vetclinic/record_list.html', {'records': records})

def record_list_filtered(request, url):
    animals = Animal.objects.get(pk=url)
    records = Record.objects.filter(animal_name=animals)
    return render(request, 'vetclinic/record_list_filtered.html', {'records': records})
