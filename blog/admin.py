from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'author', 'counted_views', 'counted_views', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    # It's prefer to Meta class
    # ordering = ('-created_date',) 
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)