from django.urls import path
from . import views
from blog.feeds import LatestEntriesFeed

app_name = 'accounts'

urlpatterns = [
    # Login
    path('login/', views.login_view, name='login'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    # Register
    path('register/', views.register_view, name='register'),
]