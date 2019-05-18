DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 设置为 mysql 数据库
        'NAME': 'lds_site_db',  # mysql 数据库名
        'USER': 'root',  # mysql 用户名，留空则默认为当前 linux 用户名
        'PASSWORD': '',  # mysql 密码
        'HOST': '127.0.0.1',  # 留空默认为 localhost
        'PORT': '',  # 留空默认为 3306 端口
        # 'CONN_MAX_AGE': 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}
