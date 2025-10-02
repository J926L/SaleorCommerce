#!/usr/bin/env python
"""Django 的命令行工具的入口。"""
import os
import sys

def main():
    """运行管理任务。"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Saleor_commerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django。您确定它已经安装并添加到您的 PYTHONPATH 环境变量中了吗？"
            "您是否忘记激活虚拟环境？"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
