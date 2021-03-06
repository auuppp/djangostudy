"""
Django settings for testcrud project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=rx0k^(!)kw##1syv_5s9kq-yp)py1t64q9&jriu5*$bw4g1q)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']
APPEND_SLASH=False




# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'books',
    'template',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'testcrud.urls'

WSGI_APPLICATION = 'testcrud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'lagou',
        'USER':'root',
        'PASSWORD':'root',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE ='Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testcrud.settings")
STATIC_URL = '/static/'
TEMPLATE_DIRS = ('D:/testing/python/gyp/djangostudy/djangoTestWeb/testcrud/testcrud/templates',
'D:/testing/python/gyp/djangostudy/djangoTestWeb/testcrud/myblog',
'D:/testing/python/gyp/djangostudy/djangoTestWeb/testcrud/books',)
#staticfiles=(path.join(ROOT_PATH,'static'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
ADMINS = (
    ('auuppp', '408496353@qq.com'),
)
MANAGERS = (
    ('auuppp', '408496353@qq.com'),
)