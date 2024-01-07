"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap

from django.urls import re_path
from django.conf import settings
from django.views.generic.base import TemplateView


sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt', include('robots.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),

    # ************************************** If pathes for password reset with email be here (WE WILL NOT FACE ANY PROBLEM) otherwise we should edit some methods in (auth.view) **************************************
    # from django.contrib.auth import views as auth_views --> add to up
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # ************************************** If pathes for password reset with email be here (WE WILL NOT FACE ANY PROBLEM) **************************************
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ********************************** Active MAINTENANCE_MODE if (MAINTENANCE_MODE = True) **********************************
if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='website/coming_soon/comingsoon-countdown-bubble.html'), name='coming_soon_index'))
# ********************************** Active MAINTENANCE_MODE if (MAINTENANCE_MODE = True) **********************************