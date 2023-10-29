from django import template
from blog.models import Post, Category
from blog.views import check_published_date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag("website/website-latest.html")
def latest_posts(args=6):
    posts = check_published_date().order_by('-published_date')[:args]
    context = {'context': posts}
    return context