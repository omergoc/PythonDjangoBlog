from blogapp.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'siberataydb',
       'USER': 'postgres',
       'PASSWORD': 'toor',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]