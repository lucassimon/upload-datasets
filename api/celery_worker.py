# Python
from os import getenv
from os.path import dirname, isfile, join

# Third
from dotenv import load_dotenv

# Apps

_ENV_FILE = join(dirname(__file__), ".env")

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)
from apps import create_app, celery
from apps.celery_utils import init_celery


app = create_app(getenv("FLASK_ENV") or "default")
init_celery(celery, app)
