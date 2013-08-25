"""
Production and global settings.
"""

import os

from . import base
from urlparse import urlparse

_db_url = urlparse(os.environ.get('DATABASE_URL', ''))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': _db_url.path[1:],
        'USER': _db_url.username,
        'PASSWORD': _db_url.password,
        'HOST': _db_url.hostname,
        'PORT': _db_url.port,
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

STATIC_URL = "/static/"

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False
