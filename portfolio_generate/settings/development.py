from .base import *

# Secret Key
SECRET_KEY = env.str('SECRET_KEY', default='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')

# Static
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

# Debug
DEBUG = env.bool('DEBUG', default=True)

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
        'POST': env.str("POSTGRES_POST"),
    }
}
