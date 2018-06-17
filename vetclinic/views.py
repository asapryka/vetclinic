from django.shortcuts import render
from django.utils import timezone
from .models import Post

def record_list(request):
    posts = Post.objects.filter(visit_date__lte=timezone.now()).order_by('visit_date')
    return render(request, 'vetclinic/record_list.html', {'posts': posts})