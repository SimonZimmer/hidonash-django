from .base import *


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mysecret'

try:
    from .local import *
except ImportError:
    pass
