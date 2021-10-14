from os import environ
from django.core.exceptions import ImproperlyConfigured


def get_env_var(key):
    try:
        return environ[key]
    except KeyError:
        raise ImproperlyConfigured(f"Missing {key} environment variable.")
