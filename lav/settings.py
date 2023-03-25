"""This contains the settings for the main Django application
need to add each new app to the list of Installed Apps """

import os

import django_heroku
import environ

env = environ.Env()
environ.Env.read_env()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", True)

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "crispy_forms",
    "website.apps.WebsiteConfig",
    "portal.apps.PortalConfig",
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "lav.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lav.wsgi.application"

DATABASES = {"default": env.db("DATABASE_URL")}

# Override the default Django user model
AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Where `./manage.py collectstatic` will store the compiles static assets.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Where static assets will be served from.
STATIC_URL = "/static/"
# Used for profile pics / images
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "website_home"
LOGIN_URL = "login"

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Enable gzip functionality for static files.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Initialise Heroku settings. If DEBUG is enabled, honour the database configuration in
# settings.py. This resolves an issue where django_heroku.settings() attempts to enable
# SSL for local Postgres database connections, even if the local DB doesn't support SSL.
django_heroku.settings(locals(), databases=(env("ENVIRONMENT") == "production"))
