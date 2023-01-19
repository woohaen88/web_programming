from .common import *


def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.strip()
    file.close()
    return secret


SECRET_KEY = read_secret("DJANGO_SECRET_KEY")

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": read_secret("MYSQL_DATABASE"),
        "USER": "root",
        "PASSWORD": read_secret("MYSQL_ROOT_PASSWORD"),
        "HOST": "mysqlDB",
        "PORT": "3306",
    }
}
