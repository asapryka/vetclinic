from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Record


def index(request):
    return render(request, 'vetclinic/index.html')

def record_list(request):
    records = Record.objects.all().order_by('visit_date')
    return render(request, 'vetclinic/record_list.html', {'records': records})
