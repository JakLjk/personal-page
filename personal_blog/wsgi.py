"""
WSGI config for personal_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_blog.settings')

application = get_wsgi_application()

from whitenoise import WhiteNoise
from pathlib import Path

application = WhiteNoise(application, root=os.path.join(Path(__file__).resolve().parent.parent, "staticfiles"))