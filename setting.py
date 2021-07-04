STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_en)]
VENV_PATH = os.path.dirname(BASE_DIR) 
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') 
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root') 
AUTH_USER_MODEL = 'account.User'
