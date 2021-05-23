from segments.settings import *

INSTALLED_APPS += [

    # Third-Party Integrations
    'rest_framework',
    'drf_yasg',

]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}