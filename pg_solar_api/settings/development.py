from .base import *

# Enable debugging for development
DEBUG = True

# Development CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Additional static files directory
STATICFILES_DIRS = [BASE_DIR / "static"]
