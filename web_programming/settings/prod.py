import os
from .common import *


DEBUG = os.getenv("DEBUG") in ["t", "True", "true", "1", "on"]

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("SECRET_KEY")


DATABASES = {
    "default": {
        "ENGINE": os.getenv("SQL_ENGINE"),
        "NAME": os.getenv("SQL_NAME"),
        "USER": os.getenv("SQL_USER"),
        "PASSWORD": os.getenv("SQL_PASSWORD"),
        "HOST": os.getenv("SQL_HOST"),
        "PORT": os.getenv("SQL_PORT"),
    }
}

CSRF_TRUSTED_ORIGINS = [
    "https://www.woohaen88-webapp.com",
    "http://www.woohaen88-webapp.com",
]
