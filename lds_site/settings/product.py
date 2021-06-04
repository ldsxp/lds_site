from .base import *  # NOQA
from .db_psycopg2 import DATABASES

DEBUG = False

ADMINS = MANAGERS = (
    ('lds', '85176878@qq.com'),  # 你的邮件地址
)

# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True

# Email 设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'  # 邮箱SMTP服务器(邮箱需要开通SMTP服务)
EMAIL_PORT = 25  # 邮箱SMTP服务端口
EMAIL_HOST_USER = '85176878@qq.com'  # 邮箱帐号
EMAIL_HOST_PASSWORD = ''  # 授权码
EMAIL_SUBJECT_PREFIX = 'website_dubug'  # 为邮件标题的前缀,默认是'[django]'
# 是否使用了SSL 或者TLS 安全链接，这里必须是 True，否则发送不成功
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# 默认发件人，不设置的话 django 默认使用的 webmaster@localhost
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER  # 设置发件人

'''
发送邮件配置
# 1.开启服务(POP3/SMTP服务)(IMAP/SMTP服务)，并且生成授权码，在第三方客户端登录时，需要授权码。
# 2.设置发送邮件配置信息，见上面 Email 设置

发送邮件例子：

    from django.conf import settings
    from django.core.mail import send_mail  # 导入 django 发送邮件模块

    email_from = settings.EMAIL_HOST_USER

    email_title = '邮件标题2'
    email_body = '邮件内容2'
    to_email = '85176878@qq.com'  # 对方的邮箱

    send_status = send_mail(email_title, email_body, email_from, [to_email])

    if send_status:
        print('发送成功')


    发送邮件最简单的方法是使用django.core.mail.send_mail()。

    # send_mail 的 subject、message、from_email和 recipient_list 参数是必须的。
    # subject：一个字符串。
    # message：一个字符串。
    # from_email：一个字符串。
    # recipient_list：一个由邮箱地址组成的字符串列表。recipient_list 中的每一个成员都会在邮件信息的“To:”区域看到其它成员。
    # fail_silently: 一个布尔值。如果设置为 False, send_mail 将引发一个 smtplib.SMTPException异常. 查看 smtplib 文档中列车出的所有可能的异常， 它们都是 SMTPException的子类。
    # auth_user: 可选的用户名用来验证SMTP服务器。如果没有提供这个值， Django 将会使用settings中 EMAIL_HOST_USER 的值。
    # auth_password: 可选的密码用来验证 SMTP 服务器。如果没有提供这个值， Django 将会使用settings中 EMAIL_HOST_PASSWORD 的值。
    # connection: 可选的用来发送邮件的电子邮件后端。如果没有指定，将使用缺省的后端实例。查看 Email backends 文档来获取更多细节。
    # html_message: 如果提供了 html_message ，会导致邮件变成 multipart/alternative ， message 格式变成 text/plain ， html_message 格式变成 text/html 。
    # 返回值将是成功传递的消息的数量（可以是0或1，因为它只能发送一个消息）。

'''

# 日志配置 https://docs.djangoproject.com/en/3.1/topics/logging/
# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')
# 如果地址不存在，则自动创建log文件夹
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # False 禁用已经存在的logger实例
    'formatters': {  # 配置打印日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s.%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'},
        'standard2': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'},
    },
    'filters': {  # 过滤器
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {  # 定义具体处理日志的方式
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # 发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],  # 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'default': {  # 默认记录所有日志(需要创建对应的目录，否则会出错)
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'error-{}.log'.format(datetime.now().strftime('%Y-%m-%d'))),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种 formatters 日志格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        'error': {  # 输出错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'error-{}.log'.format(datetime.now().strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        'info': {  # 输出info日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'info-{}.log'.format(datetime.now().strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
        'console': {  # 输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'filters': ['require_debug_true'],
            'formatter': 'standard',
        },
    },
    'loggers': {  # 用来配置用那种handlers来处理日志，比如你同时需要输出日志到文件、控制台。
        # 'django': { # loggers类型为"django"这将处理所有类型日志。
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
        'django': {  # 类型 为 django 处理所有类型的日志， 默认调用
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['default', 'error', 'mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'log': {  # log 调用时需要当作参数传入
        #     'handlers': ['error', 'info', 'console', 'default'],
        #     'level': 'INFO',
        #     'propagate': True
        # },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
