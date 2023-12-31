"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_summernote',
    'captcha',
    'robots',
    'taggit',
    'debug_toolbar',
    'website.apps.WebsiteConfig',
    'blog',
    'accounts',
]


# Robots configuration
ROBOTS_USE_HOST = True  # (True) --> is my robot should be show HOST name
ROBOTS_USE_SITEMAP = True # (True) --> is my robot should be show SITEMAP name

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'my_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_site.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

# DATE_INPUT_FORMATS =  ['%Y/%m/%d']

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# It's for debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Taggit module
TAGGIT_CASE_INSENSITIVE = False


# Multi captcha admin configuration (3type: simple-captcha, recaptcha, recaptcha2)
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = ""
LOGOUT_REDIRECT_URL = "accounts:login"

# ******************************** reset password with email ********************************
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"    # With console
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"         # With email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='l.o0of.war@gmail.com'
EMAIL_HOST_PASSWORD ='gwww mlzt rhyt ybze'
# ******************************** reset password with email ********************************


# ********************************** Active MAINTENANCE_MODE if (MAINTENANCE_MODE = True) **********************************
MAINTENANCE_MODE = True
# ********************************** Active MAINTENANCE_MODE if (MAINTENANCE_MODE = True) **********************************
