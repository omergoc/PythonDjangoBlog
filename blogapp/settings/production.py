from blogapp.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]

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

RECAPTCHA_PUBLIC_KEY = 'MyRecaptchaKey123'
RECAPTCHA_PRIVATE_KEY = 'MyRecaptchaPrivateKey456'