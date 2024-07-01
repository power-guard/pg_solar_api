from .base import *



DEBUG = False
SECRET_KEY = "This is the Production server."
ALLOWED_HOSTS = ['127.0.0.1']


# DATABASES = {
#     'default': {
#         'ENGINE': None,
#         'NAME': None,
#         'USER': None,
#         'PASSWORD': None,
#         'HOST': None,
#         'PORT': None,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Other production settings...
