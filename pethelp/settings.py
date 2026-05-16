import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', 'pethelp-desenvolvimento-local')
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    '127.0.0.1,localhost,.pythonanywhere.com,.onrender.com',
).split(',')
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        'https://*.pythonanywhere.com,https://*.onrender.com',
    ).split(',')
    if origin.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'animais',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pethelp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pethelp.wsgi.application'

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.environ.get('SQLITE_PATH', BASE_DIR / 'db.sqlite3'),
        }
    }

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(os.environ.get('MEDIA_ROOT', BASE_DIR / 'media'))
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'minhas_publicacoes'
LOGOUT_REDIRECT_URL = 'home'

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False').lower() == 'true'
