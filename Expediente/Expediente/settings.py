"""
Django settings for Expediente project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'otap%8pj-w!bo99ku-ewke7b&0v5&06+dj_xuv04i)j1_p_8_m'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.expediente',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Expediente.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Expediente.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'expedienteDB',
        'USER': 'postgres',
        'PASSWORD': 'system',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-sv'

TIME_ZONE = 'America/El_Salvador'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

LOGIN_REDIRECT_URL = reverse_lazy('expediente:inicio')
LOGOUT_REDIRECT_URL = reverse_lazy('iniciar_sesion')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

if DEBUG:
   INTERNAL_IPS = ('127.0.0.1', 'localhost')

   MIDDLEWARE += (
       'debug_toolbar.middleware.DebugToolbarMiddleware',
   )

   INSTALLED_APPS += (
       'debug_toolbar',
   )

   DEBUG_TOOLBAR_PANELS = [
       'debug_toolbar.panels.versions.VersionsPanel',
       'debug_toolbar.panels.timer.TimerPanel',
       'debug_toolbar.panels.settings.SettingsPanel',
       'debug_toolbar.panels.headers.HeadersPanel',
       'debug_toolbar.panels.request.RequestPanel',
       'debug_toolbar.panels.sql.SQLPanel',
       'debug_toolbar.panels.staticfiles.StaticFilesPanel',
       'debug_toolbar.panels.templates.TemplatesPanel',
       'debug_toolbar.panels.cache.CachePanel',
       'debug_toolbar.panels.signals.SignalsPanel',
       'debug_toolbar.panels.logging.LoggingPanel',
       'debug_toolbar.panels.redirects.RedirectsPanel',
   ]

   DEBUG_TOOLBAR_CONFIG = {
       'INTERCEPT_REDIRECTS': False,
   }