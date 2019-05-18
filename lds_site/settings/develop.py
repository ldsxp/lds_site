# flake8: noqa

from .base import *  # NOQA

DEBUG = True

# pip install django-debug-toolbar
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# 允许访问debug_toolbar的IP地址
INTERNAL_IPS = ['127.0.0.1']
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')
# DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r"http://code.jquery.com/jquery-2.1.1.min.js"}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs", 'lds_site.log'),  # 日志输出文件
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
