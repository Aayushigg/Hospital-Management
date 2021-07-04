import os
from pathlib import path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templetes) 
STATIC_DIR=os.path.join(BASE_DIR, 'static') 

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth,
    'django.contrib.contenttype',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'account''
]
  
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
    
USE_LION = True

USE_TZ = True
# Database

DATABASES={
         'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME' : 'django.contribute.auth.password_
    }, 
    {
        'NAME' : 'django.contribute.auth.password_
    }, 
    {   
        'NAME' : 'django.contribute.auth.password_
    }, 
    {  
        'NAME' : 'django.contribute.auth.password_
     }
     {
        'NAME' : 'django.contribute.auth.password_
      }, 

 ]

MIDDLEWARE=[

        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

ROOT_URLCONF = 'youtube.urls'

TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIR' : [os.path.join(BASE_DIR, 'template']
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.static',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

                ], 
               
            },
        }
    ],
    

STATIC_URL='/static/',
MEDIA_URL='media/'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_en)]
VENV_PATH = os.path.dirname(BASE_DIR) 
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') 
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root') 
AUTH_USER_MODEL = 'account.User'
