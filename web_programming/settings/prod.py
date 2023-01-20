from .common import *


environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

env = environ.Env(DEBUG=(bool, False))

ALLOWED_HOSTS = ["*"]

SECRET_KEY = env("SECRET_KEY")

DEBUG = False
DATABASES = {"default": env.db()}

CSRF_TRUSTED_ORIGINS = [
    "https://www.woohaen88-webapp.com",
    "http://www.woohaen88-webapp.com",
]
