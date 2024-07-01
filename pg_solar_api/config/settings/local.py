from .base import *

DEBUG = True
SECRET_KEY = "This is the local server."
ALLOWED_HOSTS = ['127.0.0.1']


# Database
# Adjust as per your database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
