from my_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5pifbi0lq+-*gbz31v&f4xh0%gyw&qxjq_80nf1#8-b27t+$q#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# INSTALLED_APPS = []


# Sites framework configuration
SITE_ID = 2 # (2) --> is my site domain's id that saved on db/site


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


# Summernote (how to allow iframe)
X_FRAME_OPTIONS = 'SAMEORIGIN'

