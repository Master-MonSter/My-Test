from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    # tag
    # category
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
    