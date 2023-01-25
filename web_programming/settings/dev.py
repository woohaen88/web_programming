from .common import *


SECRET_KEY="django-insecure-sg!9x9@w28+hj!a@r6^(f49el(kzeu$9b#w2!hrez2ymlqx=hh"

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
