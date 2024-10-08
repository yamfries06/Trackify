"""
Django settings for expensewebsite project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os 
import dj_database_url
from dotenv import load_dotenv


load_dotenv() 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$jte7-sg=izr-yc^v3i_5-lj=!=yhx*_nrdn8_f*6)_p9xo5#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['trackify-ad7x.onrender.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'expensewebsite', 
    'expenses', 
    'authentication',
    'userpreferences', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'expensewebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'expensewebsite/templates'), os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# print("DB_NAME:", os.getenv('DB_NAME'))
# print("DB_USER:", os.getenv('DB_USER'))
# print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
# print("DB_HOST:", os.getenv('DB_HOST'))

#postgresql://trackify_django_render_user:iPHCvhaR8fq9VY53OEBevtf2OOLrDPz9@dpg-crecdmlsvqrc73fi4330-a.oregon-postgres.render.com/trackify_django_render

''' 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # The environment variable should contain the full URL for Render's Postgres service
        'NAME': os.getenv('DB_NAME', 'local_db_name'),
        'USER': os.getenv('DB_USER', 'local_user'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
'''

DATABASE_URL = os.getenv('DATABASE_URL')  # This environment variable should be set in Render

if DATABASE_URL:
    try:
        DATABASES = {
            'default': dj_database_url.parse(DATABASE_URL)
        }
        print(f"Successfully parsed DATABASE_URL: {DATABASE_URL}")
        print(DATABASES)
    except ValueError as e:
        print(f"Error parsing DATABASE_URL: {e}")
        raise
else:
    raise Exception("DATABASE_URL is not set in the environment.")


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'expensewebsite/static')] # tells django where to find additioanl static files
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles') #its fine if this path doens't exist at the start -- will copy all static files from apps into this new directory
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib import messages

MESSAGE_TAGS= { 
    messages.ERROR: 'danger'
}


