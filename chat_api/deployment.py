import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware"
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_SIR ={pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split('')}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_SIR["mydatabase"],
        "HOST": CONNECTION_SIR['use'],
        "USER":CONNECTION_SIR ["mydatabase"],
        "PASSWORD":CONNECTION_SIR ["mypassword"],
        
        
    }
}
SECRET_KEY = os.environ['MY SECRET_KEY']
#CORS_ALLOWED_ORIGINS = [
    # "http://localhost:3000",  
    # "http://127.0.0.1:3000",
#]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}






STATIC_ROOT =  BASE_DIR / 'staticfiles'


