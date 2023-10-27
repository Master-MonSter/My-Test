from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name
        
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'blog/', default='blog/default.jpg')
    # tag
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date'] # ['created_date'] reverse_order
        # How to change name of the class
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title
    

    