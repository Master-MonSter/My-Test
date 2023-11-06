from django import template
from blog.models import Post, Category, Comment
from blog.views import check_published_date

register = template.Library()

@register.simple_tag(name="comments_count")
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.inclusion_tag("blog/blog-latest.html")
def latest_posts(arg=3):
    context = {'context': check_published_date().order_by('-published_date')[:arg]}
    return context

@register.inclusion_tag("blog/blog-categories.html")
def post_categories():
    posts = check_published_date()
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories': cat_dict}
    