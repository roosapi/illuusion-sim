"""
WSGI config for virtuaalitallit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

sys.path.append(settings.BASE_DIR)
sys.path.append(os.environ.get('DJANGO_VENV_PATH'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "virtuaali.settings")

application = get_wsgi_application()
