from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECRET_KEY = 'asuperS3cretK$yshouldgohere'

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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
