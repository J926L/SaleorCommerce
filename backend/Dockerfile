# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录
WORKDIR /app

# 安装系统依赖 (用于 psycopg2)
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码到工作目录
COPY . .

# 暴露端口
EXPOSE 8000

# 添加执行权限给 entrypoint 脚本
RUN chmod +x /app/entrypoint.sh

# 指定容器启动时运行的命令
ENTRYPOINT ["/app/entrypoint.sh"]
