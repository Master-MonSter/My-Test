from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post-<int:pid>', views.single_blog, name='post'),
    path('test-<int:pid>', views.test_view, name='test'),
]