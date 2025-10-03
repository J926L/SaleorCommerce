# Docker 使用指南

本项目已完全 Docker 化，允许你通过几个简单的命令来启动、管理和停止整个应用（包括后端、店面、仪表板和数据库）。这确保了在任何机器上都有一致的开发环境。

## 先决条件

请确保你的系统已安装以下软件：

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   [Git](https://git-scm.com/)

## 快速启动

按照以下步骤，即可在你的本地机器上运行整个 Saleor Commerce 平台。

**1. 克隆仓库**

```bash
git clone https://github.com/J926L/SaleorCommerce.git
cd SaleorCommerce
```

**2. 配置环境变量**

*   将项目根目录下的 `.env.docker.example` 文件复制为 `.env.docker`。
*   你需要为后端服务生成一个私有的 `SECRET_KEY`。

由于密钥需要在 Docker 容器内生成，请先运行一次构建命令：

```bash
docker-compose build backend
```

然后，运行以下命令来生成密钥：

```bash
docker-compose run --rm backend python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

*   复制终端输出的密钥，并将其粘贴到 `.env.docker` 文件的 `SECRET_KEY=` 后面，然后保存文件。

**3. 构建并启动服务**

在项目的根目录下，运行以下命令：

```bash
docker-compose up --build
```

*   `--build` 参数会强制 Docker 根据 `Dockerfile` 重新构建镜像。第一次启动时必须使用它。
*   Docker 将开始构建所有服务的镜像并依次启动它们。这个过程在第一次运行时可能需要几分钟。

**4. 访问应用**

当所有容器都成功启动后，你就可以在浏览器中访问项目的各个部分了：

*   **店面 (Storefront)**: `http://localhost:3000`
*   **仪表板 (Dashboard)**: `http://localhost:3001`
*   **后端 API (Backend)**: `http://localhost:8000/graphql/`

## 常用 Docker 命令

**停止所有服务**

当你使用完毕后，在同一个终端窗口按 `Ctrl + C`，然后运行以下命令来彻底停止并移除所有容器和网络：

```bash
docker-compose down
```

**在后台运行服务**

```bash
docker-compose up -d
```

**查看日志**

```bash
docker-compose logs -f backend
```

**创建超级用户**

```bash
docker-compose run --rm backend python manage.py createsuperuser
```

## Docker 配置概览

*   `docker-compose.yml`: 项目的核心编排文件，定义了所有服务及其关系。
*   `.env.docker.example`: Docker 环境的配置模板。
*   `backend/Dockerfile`: 定义了如何构建 Django 后端镜像。
*   `storefront/Dockerfile`: 定义了如何构建 Next.js 店面镜像。
*   `dashboard/Dockerfile`: 定义了如何构建 React 仪表板并使用 Nginx 托管。
*   `backend/entrypoint.sh`: 在后端容器启动时自动运行数据库迁移并启动 Gunicorn 服务器的脚本。
