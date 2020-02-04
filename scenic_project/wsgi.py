"""
WSGI config for scenic_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
# from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# scenic_project = os.path.expanduser('~/scenic-realty-app/scenic_project')
# load_dotenv(os.path.join(scenic_project, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scenic_project.settings')

application = get_wsgi_application()
