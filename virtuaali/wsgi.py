"""
WSGI config for virtuaalitallit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/roosa/illuusion-sim')
sys.path.append('/home/roosa/illuusion_prod/lib/python3.5/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

application = get_wsgi_application()
