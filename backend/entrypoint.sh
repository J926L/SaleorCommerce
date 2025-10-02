#!/bin/sh

# 等待数据库准备就绪
# 这个循环会一直尝试连接数据库，直到成功为止
# 注意：这需要 postgresql-client，我们已经在 Dockerfile 中安装了它
until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  echo "Waiting for database..."
  sleep 2
done

# 运行数据库迁移
python manage.py migrate

# 启动 Gunicorn 服务器
# --bind 0.0.0.0:8000 表示监听所有网络接口的 8000 端口
# Saleor_commerce.wsgi 是你的 WSGI 应用的路径
gunicorn Saleor_commerce.wsgi --bind 0.0.0.0:8000
