"""
WSGI config for smoothie_goofy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
if os.environ.has_key("HEROKU"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smoothie_goofy.settings_heroku")

    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smoothie_goofy.settings")
    application = get_wsgi_application()
