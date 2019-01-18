from .settings_defaults import *  # noqa
try:
    from .settings_local import *  # noqa
except ModuleNotFoundError:
    pass
