from .common import *


# def read_secret(secret_name):
#     file = open("/run/secrets/" + secret_name)
#     secret = file.read()
#     secret = secret.strip()
#     file.close()
#     return secret
#
#
# SECRET_KEY = read_secret("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ['*']

SECRET_KEY = env("SECRET_KEY")

DEBUG = False
DATABASES = {
    "default": env.db()
}

CSRF_TRUSTED_ORIGINS = [
    "https://www.woohaen88-webapp.com",
    "http://www.woohaen88-webapp.com",

]
