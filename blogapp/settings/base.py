from pathlib import Path
from datetime import timedelta
import os
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-146l8#o8^cfj=u&n=kv6a$g21nlc^l#g7dcvzz&hi0am*m+480'


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }
 

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=1500)
}

# Application definition

INSTALLED_APPS = [
    'captcha',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles.apps.ArticlesConfig',
    'django.contrib.sitemaps',
    'pages',
    'ckeditor',
    'settings',
    'rest_framework',
]

AUTH_USER_MODEL = "users.Account"

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'blogapp.middleware.AnonymousUserTrackingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'blogapp.slash_middleware.AppendOrRemoveSlashMiddleware',
]

ROOT_URLCONF = 'blogapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'articles.context_processors.categories_renderer',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ="smtp.gmail.com"
EMAIL_HOST_USER ="info@siberatay.com"
EMAIL_HOST_PASSWORD = "ivpadmqxmfkvazts"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "info@siberatay.com"


RECAPTCHA_PUBLIC_KEY = '6Lcp6SIiAAAAANGaVhoyl_Rq0R389ERx7ino2-BI'
RECAPTCHA_PRIVATE_KEY = '6Lcp6SIiAAAAAMQXPUbeOv4nJxBeI3_mmLAAAFb8'
RECAPTCHA_REQUIRED_SCORE = 0.85

SESSION_EXPIRE_SECONDS = 86400
SESSION_SAVE_EVERY_REQUEST = True
SESSION_TIMEOUT_REDIRECT = 'login'
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

APPEND_SLASH = True
