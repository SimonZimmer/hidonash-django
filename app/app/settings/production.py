from .base import *

import os

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = [
    'https://*.hidonash.com',
    'https://*.127.0.0.1',
    'https://95.179.203.207',
]
CORS_ORIGIN_WHITELIST = [
    'https://hidonash.com',
    'https://*.127.0.0.1',
    'https://95.179.203.207',
]

try:
    from .local import *
except ImportError:
    pass
