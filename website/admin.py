from django.contrib import admin
from website.models import Contact, NewsLetter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'created_date')
    list_filter = ('email',)
    # It's prefer to Meta class
    # ordering = ('-created_date',) 
    search_fields = ('name', 'email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter)