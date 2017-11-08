from signlogin.settings.base import *


#overrride base.py settings here
DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #
    }
}


try:
    from signlogin.settings.local import * #ignored by git so not committed to the repository
except:
    pass
