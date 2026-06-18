import os
import dj_database_url
from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = [
    'passpilot-backend.onrender.com',
    'passpilot-backend-etcp.onrender.com',
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}

CSRF_TRUSTED_ORIGINS = [
    'https://passpilot-backend.onrender.com',
]

CORS_ALLOWED_ORIGINS = [
    'https://passpilot-backend.onrender.com',
]