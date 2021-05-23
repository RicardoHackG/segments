from .common import *

PREPEND_WWW = False
DEBUG = True

PROJECT_URL = 'http://0.0.0.0:9000'
ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS += (
    'django_extensions',
)

ROOT_URLCONF = 'segments.admin.urls'
