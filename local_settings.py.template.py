from virtuaali.settings import *

SECRET_KEY = '&(yuno%$i08g5jcux+l@^pz$&e@uf)43-)m739z1o==c)g%f8)'
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'illuusion-sim',
        'USER': 'hopeapaju',
        'PASSWORD': 'hopeapaju',

    }
}
