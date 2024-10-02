"""
WSGI config for restaurantazure project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from .settings import BASE_DIR
from django.conf import settings
from django.core.wsgi import get_wsgi_application
#from whitenoise import WhiteNoise

#settings_module = 'restaurantazure.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'restaurantazure.settings'
# trash
settings_module = 'restaurantazure.deployment'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
#application = WhiteNoise(get_wsgi_application(), root=os.path.join(BASE_DIR, 'staticfiles'))