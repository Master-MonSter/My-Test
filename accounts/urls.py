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
    path('signup/', views.register_view, name='signup'),
    
    # Password change
    path('change_password/', views.change_password_view, name='change_password'),
]
    