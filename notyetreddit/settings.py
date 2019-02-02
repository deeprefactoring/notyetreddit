import django_heroku
from .settings_defaults import *  # noqa
django_heroku.settings(locals())
try:
    from .settings_local import *  # noqa
except ModuleNotFoundError:
    pass
