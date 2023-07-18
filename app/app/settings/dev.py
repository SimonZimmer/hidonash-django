from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECRET_KEY = '+u72mnv22dh2s3vxlpu+e_mmqfu)_wi=-#2y(n%^%410gx6rby'


try:
    from .local import *
except ImportError:
    pass
