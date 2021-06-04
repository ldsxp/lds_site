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
