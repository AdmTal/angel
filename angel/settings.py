"""
Django settings for angel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
from os import path, environ

import os

BASE_DIR = path.dirname(path.dirname(__file__)) 


def get_env_variable(var_name):
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the %s enviroment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('ANGEL_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

### Set the path to our current one
PROJECT_DIR = Path(__file__).ancestor(3)  ### root of the project
MEDIA_DIR = PROJECT_DIR.child('media')  ### where dynamic media (user uploads) are stored
TEMPLATE_DIR = PROJECT_DIR.child('templates')  ### where our templates are stored
STATIC_MEDIA_DIR = PROJECT_DIR.child('static')  ### where our static media is stored

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'south',
    'storages',
    'boto',
    'users',
    'outfits',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_DIR,
    'templates',
)

ROOT_URLCONF = 'angel.urls'

WSGI_APPLICATION = 'angel.wsgi.application'
WSGI_APPLICATION = 'angel.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Pages that require auth will redirect here when user is not authenticated
LOGIN_URL = '/login/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = MEDIA_DIR


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = STATIC_MEDIA_DIR


PROJECT_PATH = path.dirname(path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    path.join(PROJECT_PATH, 'static'),
)

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DOMAIN = 'angelhack2014.herokuapp.com'

# Static asset configuration

AWS_STORAGE_BUCKET_NAME = 'angelhack2014'
AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATIC_URL = S3_URL