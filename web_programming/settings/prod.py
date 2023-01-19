from .common import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Take environment variables from .env file
# PRODUCT:
# environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# TEST


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env("DEBUG")
# TEST
DEBUG = False

ALLOWED_HOSTS = ["*"]

# PRODUCT
# DATABASES = {
#     "default": env.db(),
# }
# TEST
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
