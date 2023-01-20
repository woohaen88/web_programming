from .common import *


environ.Env.read_env(os.path.join(BASE_DIR, ".env.dev"))

env = environ.Env(DEBUG=(bool, False))


SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": env.db()}
