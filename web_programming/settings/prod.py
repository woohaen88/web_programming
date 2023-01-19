from .common import *

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "mysqlDB",
        "PORT": "3306",
    }
}
