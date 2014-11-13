"""
Django settings for dota2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v49ym7m1hy*b28y&x0j(h7r3$_b=y(bubo#nmhsf)-g3n9+ep_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
#sys.path.insert(0, os.path.join(BASE_DIR, 'dota2/apps'))
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
	'dota2.apps.app1',
    'dota2.apps.app2',
    'dota2.apps.login',
     'bootstrap3',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dota2.urls'

WSGI_APPLICATION = 'dota2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dota2',
		'USER': 'dota2',
		'PASSWORD': 'dota2',
		'HOST':'',
		'PORT':'', 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
TEMPLATE_DIRS = (
    # '%s/dota2/apps/app1/templates' %BASE_DIR,
    # '%s/dota2/apps/app2/templates' %BASE_DIR,
    # '%s/dota2/apps/app2/templates' %BASE_DIR,

)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = 'media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '%s/media' % BASE_DIR

# The URL that handles the media, static, etc.
STATIC_ROOT = ''

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static/'),
)

# AUTHENTICATION_BACKENDS = (
#     'social.backends.steam.SteamOpenId',
#     'django.contrib.auth.backends.ModelBackend',
# )
# SOCIAL_AUTH_SANITIZE_REDIRECTS = False
# LOGIN_REDIRECT_URL = 'http://llovebaimuda.herokuapp.com/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://llovebaimuda.herokuapp.com/'
# SOCIAL_AUTH_WEIBO_LOGIN_REDIRECT_URL = 'http://llovebaimuda.herokuapp.com/'

# AUTHENTICATION_BACKENDS = (
#   'social_auth.backends.contrib.github.GithubBackend',
#   'django.contrib.auth.backends.ModelBackend',
# )
#
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'social_auth.context_processors.social_auth_by_type_backends',
#     'social_auth.context_processors.social_auth_login_redirect',
# )
#
# SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# SOCIAL_AUTH_UID_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
# SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
# SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
#
# SOCIAL_AUTH_ENABLED_BACKENDS = ('github',)
#
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/members/'
# LOGIN_ERROR_URL = '/login-error/'
#
#
#
# GITHUB_API_KEY = '2c9c4ef0200a6ac0691f'
# GITHUB_API_SECRET = '4ce11420819c133cee2ddab4fc9be165db642609'
#
# SOCIAL_AUTH_WEIBO_KEY ='3257697480'
#
# SOCIAL_AUTH_WEIBO_SECRET='79aa66a53c97de81ba84118125cde021'

#SOCIAL_AUTH_STEAM_API_KEY = '614588240E6C5CF7A86BA321C78C5475'
