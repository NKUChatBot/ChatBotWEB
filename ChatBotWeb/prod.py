# 导入公共配置
from .settings import *

# 生产环境关闭DEBUG模式
DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/www/ctfsite/ctfsite_debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# 生产环境开启跨域
CORS_ORIGIN_ALLOW_ALL = True
