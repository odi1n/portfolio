from .base import *

if env.str('ENVIRONMENT') == 'production':
    from .production import *  # noqa
else:
    from .development import *  # noqa
