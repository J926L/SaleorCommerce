# Django 项目 'Saleor_commerce' 的设置文件。

import os
from pathlib import Path
from dotenv import load_dotenv

# 构建项目内部的路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 从 .env 文件加载环境变量
load_dotenv(BASE_DIR / '.env')

# 安全警告：在运行前必须在你的环境中设置一个私有的 SECRET_KEY。
# 不要将生产密钥提交到版本控制中。
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    raise Exception('错误：请在 .env 文件中设置 SECRET_KEY。参考 backend/README.md 文件中的说明。')


# 对于练习项目，DEBUG=True 是可以接受的。
DEBUG = True

# 允许本地主机访问
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 应用程序定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'corsheaders',
    'product.apps.ProductConfig', # 产品应用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Saleor_commerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Saleor_commerce.wsgi.application'

# 数据库
# 对于练习项目，SQLite 是一个很好的选择。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 密码验证
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

# 国际化
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件 (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Graphene-Django 设置
GRAPHENE = {
    'SCHEMA': 'Saleor_commerce.schema.schema',
}

# 跨域资源共享设置
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # 你的店面地址
    "http://localhost:3001", # 你的仪表板地址
]
