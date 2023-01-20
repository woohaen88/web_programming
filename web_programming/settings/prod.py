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


SECRET_KEY = env("SECRET_KEY")

DEBUG = False
DATABASES = {
    "default": env.db()
}
