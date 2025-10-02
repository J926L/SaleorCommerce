# Saleor_commerce 项目的 WSGI 配置文件。

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Saleor_commerce.settings')

application = get_wsgi_application()
