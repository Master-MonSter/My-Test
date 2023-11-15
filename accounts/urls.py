from django.urls import path
from . import views
from blog.feeds import LatestEntriesFeed
from django.contrib.auth import views as auth_views

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

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
    