from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from datetime import datetime
from django.utils import timezone

def check_published_date():
    now = datetime.now()

    # Now time with timezone
    now = timezone.make_aware(datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))

    # Now time without timezone
    # now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    posts = Post.objects.filter(published_date__lte=now)
    print(now)
    context = {'context': posts}
    return context

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def json_test(request):
    return JsonResponse({'name': 'Mr.BoO', 'description': 'Scary funny little ghost'})