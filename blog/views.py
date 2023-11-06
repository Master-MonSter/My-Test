from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# How to get the current timezone
# from django.utils.timezone import get_current_timezone
# tzname = get_current_timezone()

def check_published_date():
    # Now time with timezone
    now = datetime.now()
    now = timezone.make_aware(datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))
    # Now time without timezone
    # now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    posts = Post.objects.filter(published_date__lte=now, status=1)
    return posts

def index_view(request, **kwargs):
    posts = check_published_date()
    # Category validation ***********************************************************************************
    if kwargs is not None:
        if kwargs.get('cat_name') is not None:
            posts = posts.filter(category__name=kwargs['cat_name'])
        elif kwargs.get('author_username') is not None:
            posts = posts.filter(author__username=kwargs['author_username'])
        elif kwargs.get('tag_name') is not None:
            posts = posts.filter(tag__name=kwargs['tag_name'])
    # Category validation ***********************************************************************************
    # Search validations *************************************************************************************
    if request.method == 'GET':
        if x:= request.GET.get('sBar'):
            posts = posts.filter(content__contains=x)
    # Search validations *************************************************************************************
    # Pagination *********************************************************************************************
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    # Pagination *********************************************************************************************

    context = {'context': posts}
    return render(request, 'blog/blog-home.html', context)

def single_blog(request, pid):
    posts = check_published_date()
    # print("all posts: " + str(posts))
    context = get_object_or_404(posts, pk=pid)
    context.counted_views = context.counted_views + 1
    context.save()
    # Finding the post before and after
    nextPost = posts.filter(pk__gt=pid).first()
    prevPost = posts.filter(pk__lt=pid).last()
    # print("       prev" + str(prevPost)+ "       next" + str(nextPost) + "       context" + str(context))
    # print(type(nextPost))
    context = {'context': context, 'prevPost': prevPost, 'nextPost': nextPost}
    return render(request, 'blog/blog-single.html', context)

def test_view(request, pid):
    posts = check_published_date()
    context = get_object_or_404(posts, pk=pid)
    print(context)
    context = {'context': context}
    return render(request, 'test.html', context)

def blog_search(request):
    posts = check_published_date()
    if request.method == 'GET':
        if x:= request.GET.get('sBar'):
            posts = posts.filter(content__contains=x)
    context = {'context': posts}
    return render(request, 'blog/blog-home.html', context)
