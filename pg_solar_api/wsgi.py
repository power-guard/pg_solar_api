import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "pg_solar_api.settings.development"
)
if os.getenv("DJANGO_ENV") == "production":
    os.environ["DJANGO_SETTINGS_MODULE"] = "pg_solar_api.settings.production"

application = get_wsgi_application()
