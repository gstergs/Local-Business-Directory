# settings.py

import os
from pathlib import Path

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')  # Ensure this is secure in production
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = []  # Add allowed hosts for production

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin interface
    'django.contrib.auth',  # Authentication framework
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static files framework
    'crispy_forms',  # Form rendering helper
    'crispy_bootstrap4',  # Bootstrap 4 integration for crispy_forms
    'businesses',  # Custom app for businesses
    'accounts',  # Custom app for user accounts
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session management
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# URL configuration
ROOT_URLCONF = 'Local_business_directory.urls'  # URL configuration module

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django template engine
        'DIRS': [BASE_DIR / 'templates'],  # Directory for project-level templates
        'APP_DIRS': True,  # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'Local_business_directory.wsgi.application'  # WSGI application for deployment

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the SQLite database file
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Similarity validator
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Minimum length validator
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Common password validator
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Numeric password validator
]

# Localization
LANGUAGE_CODE = 'en-us'  # Language code
TIME_ZONE = 'UTC'  # Time zone
USE_I18N = True  # Enable internationalization
USE_L10N = True  # Enable localization
USE_TZ = True  # Enable timezone support

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL for static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directory for additional static files

# Media files (user-uploaded content)
MEDIA_URL = '/media/'  # URL for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for media files

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default primary key field type

# Crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Template pack for crispy_forms

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'  # Custom user model

# Login and logout redirects
LOGIN_REDIRECT_URL = '/'  # Redirect URL after login
LOGOUT_REDIRECT_URL = '/'  # Redirect URL after logout
