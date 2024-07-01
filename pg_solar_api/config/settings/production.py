from .base import *



DEBUG = False
SECRET_KEY = "This is the Production server."
ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': None,
        'NAME': None,
        'USER': None,
        'PASSWORD': None,
        'HOST': None,
        'PORT': None,
    }
}

# Other production settings...
