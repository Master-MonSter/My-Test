from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
from django.utils import timezone

# How to get the current timezone
# from django.utils.timezone import get_current_timezone
# tzname = get_current_timezone()

def check_published_date():
    now = datetime.now()

    # Now time with timezone
    now = timezone.make_aware(datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))

    # Now time without timezone
    # now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    posts = Post.objects.filter(published_date__lte=now)
    print(posts)
    return posts

def index_view(request):
    context = {'context': check_published_date()}
    return render(request, 'blog/blog-home.html', context)

def single_blog(request, pid):
    posts = check_published_date()
    context = get_object_or_404(posts, pk=pid)
    context.counted_views = context.counted_views + 1
    context.save()
    print(context)
    context = {'context': context}
    return render(request, 'blog/blog-single.html', context)

def test_view(request, pid):
    posts = check_published_date()
    context = get_object_or_404(posts, pk=pid)
    print(context)
    context = {'context': context}
    return render(request, 'test.html', context)

