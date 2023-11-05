from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import Post
from blog.views import check_published_date
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return check_published_date()

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
        return reverse('blog:post', kwargs={'pid': item.id})