from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post-<int:pid>', views.single_blog, name='post'),
    path('category-<str:cat_name>', views.index_view, name='category'),
    path('author-<str:author_username>', views.index_view, name='author'),
    path('search/', views.index_view, name='search'),
    path('test-<int:pid>', views.test_view, name='test'),
]