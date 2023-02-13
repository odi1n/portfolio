from .base import *

# Secret Key
SECRET_KEY = env.str('SECRET_KEY', default='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')

# Debug
DEBUG = env.bool('DEBUG', default=True)

# TimeZone
TIME_ZONE = env.str('TIME_ZONE', default='Europe/Moscow')

# Allowed
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='*')

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
