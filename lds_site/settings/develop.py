# flake8: noqa

from .base import *  # NOQA

DEBUG = True

# pip install django-debug-toolbar
INSTALLED_APPS += [
    'debug_toolbar',
    'pympler',
    'debug_toolbar_line_profiler',
    # 'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

# 允许访问debug_toolbar的IP地址
INTERNAL_IPS = ['127.0.0.1']
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')
# DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r"http://code.jquery.com/jquery-2.1.1.min.js"}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    # 上面是默认设置
    # djdt_flamegraph 火焰图 应该不支持 django 2.2
    # 'djdt_flamegraph.FlamegraphPanel',
    # 'debug_toolbar.panels.timer.TimerPanel',
    # pympler 内存占用分析
    # 'pympler.panels.MemoryPanel',
    # django-debug-toolbar-line-profiler 行级性能分析插件
    # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
]

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
