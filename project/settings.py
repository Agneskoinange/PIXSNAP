import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku
# import dj_database_url
# from decouple import config,Csv

CSRF_TRUSTED_ORIGINS = ['https://heroku.com']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-$y%)ix#56=-%j18ni$*p-7h_pjbxqpd^nb04zl19@v@!a=$dxo'
SECRET_KEY='pixsnap1234'

    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'bootstrap3',
    'cloudinary',

]

MIDDLEWARE = [
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'pixsnap',
           'USER': 'nessie',
           'PASSWORD': 'agnes1234',
           'PORT': '',
       }
}     

# MODE=config("MODE", default="dev")
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# development
# if config('MODE')=="dev":
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql',
#            'NAME': config('DB_NAME'),
#            'USER': config('DB_USER'),
#            'PASSWORD': config('DB_PASSWORD'),
#            'HOST': config('DB_HOST'),
#            'PORT': '',
#        }
       
#    }
# # production
# else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }




# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# DATABASES = { 'default': dj_database_url.config(default='postgres://nessie:agnes1234@localhost/pixsnap') }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = 'staticfiles'
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# adding config
cloudinary.config( 
  cloud_name = "dopvdc9a1", 
  api_key = "392671715629863", 
  api_secret = "arHv5ZYdNf0Z8biPJ7gCSuHKXxU" 
)

# Configure Django App for Heroku.
django_heroku.settings(locals())