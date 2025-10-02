# Saleor_commerce 项目的 ASGI 配置文件。

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Saleor_commerce.settings')

application = get_asgi_application()
