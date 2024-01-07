from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('index', views.comingsoon_view, name='coming_soon_index'),
    # path('index', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('newsletter', views.newsletter_view, name='newsletter'),
    path('json', views.json_test)
    # path('admin/', admin.site.urls),
]