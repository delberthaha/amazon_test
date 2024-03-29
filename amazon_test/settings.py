"""
Django settings for amazon_test project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(1&1_(k3%w!4-1vgz%@c@2t8s7gl@f+#$ont@myyk=nrr(sy_7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'amazon.apps.AmazonConfig'
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

ROOT_URLCONF = 'amazon_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'amazon_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
os.environ['AWS_ENV'] = 'SANDBOX'

credentials = dict(
    refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
    lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
    lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487',
    aws_access_key='AKIAZ2ETATIEAD2VJISF',
    aws_secret_key='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',
    role_arn='arn:aws:iam::674618186248:role/silk_test',
)

SPAPI_CRIDENTIALS = credentials
