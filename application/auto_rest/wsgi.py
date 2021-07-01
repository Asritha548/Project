"""
WSGI config for auto_rest project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_MODULE", "auto_rest.settings")

application = get_wsgi_application()
