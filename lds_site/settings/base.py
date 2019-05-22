"""
Django settings for lds_site project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 因为我们把设置放在了目录中
BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

sys.path.insert(0, os.path.join(BASE_DIR, 'lib'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
print('BASE_DIR：', BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zqo)#!947n02%q_zc$-0emy^np0_2b1d@_d1u@y(p)$8-96sld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize',  # 添加人性化过滤器
    # 'django.contrib.sitemaps',  # 网站地图
    'ckeditor',
    'ckeditor_uploader',
    'xadmin',
    'crispy_forms',
    # 应用程序
    'blog',
    'config',
    'comment',
]

MIDDLEWARE = [
    'blog.middleware.user_id.UserIDMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lds_site.urls'

THEME = 'bootstrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/themes', THEME)]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lds_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 语言

TIME_ZONE = 'Asia/Shanghai'  # 时区

USE_I18N = True  # 语言

USE_L10N = True  # 数据和时间格式

USE_TZ = True  # 启用时区

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 使用 collectstatic 命令收集静态文件时，存放 static 文件的路径
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # .replace('\\', '/')

STATICFILES_DIRS = (
    # 默认Django会在每个app下的static/app查找静态文件
    # 如果加额外的路径寻找则在STATICFILES_DIR中设置（设置这个，因为项目共用bootstrap）
    os.path.join(BASE_DIR, "static"),
)

# xadmin 设置
XADMIN_TITLE = 'lds管理后台'
XADMIN_FOOTER_TITLE = 'power by lds'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
        'tabSpaces': 4,
    },
}
CKEDITOR_UPLOAD_PATH = "article_images"
