# PostgreSQL ,需要安装 psycopg2 模块
# pip install psycopg2
# linux 用 psycopg2-binary 替换 不过这个是建议开发用
# pip install psycopg2-binary

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lds_site_db',  # 数据库名字(需要先创建)
        'USER': 'lds',  # 登录用户名
        'PASSWORD': '',  # 密码
        'HOST': '127.0.0.1',  # 数据库IP地址,留空默认为localhost
        'PORT': '5432',  # 端口
    }
}
