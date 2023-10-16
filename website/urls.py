from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('json', views.json_test)
    # path('admin/', admin.site.urls),
]