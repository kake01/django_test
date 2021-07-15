import os
from pathlib import Path


SECRET_KEY = 'django-insecure-khxjqmqw6($rtn2h2-#l#88vf&&)1_esvw4*59=6ds-)h+i^9n'

#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True #ローカルでDebugできるようになります