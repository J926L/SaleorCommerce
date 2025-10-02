# product 应用程序的配置

from django.apps import AppConfig


class ProductConfig(AppConfig):
    """产品应用的配置"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    verbose_name = '产品管理' # 在 Django admin 中显示的名称
