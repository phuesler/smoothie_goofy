"""
WSGI config for smoothie_goofy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
if not os.environ.has_key("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smoothie_goofy.settings")


from django.core.wsgi import get_wsgi_application
if os.environ.has_key("HEROKU"):
    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()
