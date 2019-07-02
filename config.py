import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'library',
        'host': 'mongodb://localhost/library'
    }

    LOGGING_PATH = "log"

