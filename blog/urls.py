from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('single', views.single_blog, name='single'),
    path('test', views.test_view, name='test'),
]