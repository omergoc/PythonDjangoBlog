from blogapp.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["78.135.107.100"]

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'siberataydb',
       'USER': 'kaptantr',
       'PASSWORD': '7P$Y2UW#C$%O',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')