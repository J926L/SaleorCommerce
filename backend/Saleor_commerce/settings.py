# Django 项目 'Saleor_commerce' 的设置文件。

import os
from pathlib import Path
from dotenv import load_dotenv

# 构建项目内部的路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 根据环境加载不同的 .env 文件
# 在 Docker 中，我们使用 .env.docker
if os.environ.get('DOCKER_ENV') == 'true':
    load_dotenv(BASE_DIR / '.env.docker')
else:
    load_dotenv(BASE_DIR / '.env')

# 安全警告：在运行前必须在你的环境中设置一个私有的 SECRET_KEY。
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    raise Exception('错误：请在 .env 文件或 .env.docker 文件中设置 SECRET_KEY。')


DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'backend']


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
    'product.apps.ProductConfig',
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

# 数据库配置
# 默认使用 SQLite，但如果设置了数据库环境变量，则使用 PostgreSQL
DB_ENGINE = os.environ.get('DB_ENGINE')
if DB_ENGINE:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
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
    "http://localhost:3000",
    "http://localhost:3001",
]
