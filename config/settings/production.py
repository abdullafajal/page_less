
from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Database
if os.getenv("DATABASE_URL"):
    DATABASES["default"] = dj_database_url.config(conn_max_age=600)
