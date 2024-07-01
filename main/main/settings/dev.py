from .base import *
from ..urls import urlpatterns
from django.urls import path, include

DEBUG = env("DEBUG_DEV")

INSTALLED_APPS+=['django_extensions','']
urlpatterns+=[path("__debug__/", include("debug_toolbar.urls")),]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]