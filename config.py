import os

true_values_set = {"1", "true", "True", "yes", "Y", "on"}


def read_bool_from_os_env(name, default=False):
    v = os.environ.get(name)
    if v is not None:
        if v in true_values_set:
            return True
        else:
            return False
    else:
        return default


class Config:
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SECONDS_IN_HOUR = 60 * 60
    SECONDS_IN_DAY = SECONDS_IN_HOUR * 24

    SESSION_TIMEOUT = SECONDS_IN_DAY * 10

    WTF_CSRF_ENABLED = False

    SECRET_KEY = os.environ.get("SECRET_KEY")
