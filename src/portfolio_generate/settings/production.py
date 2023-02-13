from .base import *

# Secret Key
SECRET_KEY = env.str('SECRET_KEY')

# Debug
DEBUG = env.bool('DEBUG')

# Allowed
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database Setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("POSTGRES_HOST"),
        'POST': env.str("POSTGRES_PORT"),
    }
}
