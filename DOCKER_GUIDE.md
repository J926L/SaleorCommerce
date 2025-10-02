# Docker 使用指南

本项目已完全 Docker 化，允许你通过几个简单的命令来启动、管理和停止整个应用（包括后端、店面、仪表板和数据库）。这确保了在任何机器上都有一致的开发环境。

## 先决条件

请确保你的系统已安装以下软件：

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   [Git](https://git-scm.com/)

## 快速启动

按照以下步骤，即可在你的本地机器上运行整个 Saleor Commerce 平台。

**1. 克隆仓库**

如果你还没有克隆项目，请先克隆：

```bash
git clone https://github.com/J926L/SaleorCommerce.git
cd SaleorCommerce
```

**2. 配置环境变量**

后端服务需要一个私有的 `SECRET_KEY` 才能安全运行。

*   打开 `backend/.env.docker` 文件。
*   你需要生成一个新的密钥来替换占位符 `your-secret-key-goes-here`。

你可以通过在终端运行以下 Python 命令来快速生成一个安全的密钥：

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

*   复制生成的密钥，并将其粘贴到 `.env.docker` 文件中，然后保存文件。例如：

    ```env
    SECRET_KEY='p@d)2$b5m!q-z+x&n*c)k@l^s&o!w#y$t(r@u*e&f'
    ```

**3. 构建并启动服务**

在项目的根目录（即 `docker-compose.yml` 文件所在的目录）下，运行以下命令：

```bash
docker-compose up --build
```

*   `--build` 参数会强制 Docker 根据 `Dockerfile` 重新构建镜像。第一次启动时必须使用它。后续如果修改了 `Dockerfile` 或 `requirements.txt` 等文件，也需要使用此参数。
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

如果你希望服务在后台运行，而不是占据你的终端窗口：

```bash
docker-compose up -d
```

**查看日志**

实时查看特定服务的日志对于调试非常有用。例如，查看后端服务的日志：

```bash
docker-compose logs -f backend
```

**创建超级用户**

由于服务在容器内运行，你需要使用 `docker-compose run` 来执行 `manage.py` 命令。例如，创建一个 Django 超级用户：

```bash
docker-compose run --rm backend python manage.py createsuperuser
```

*   `--rm` 参数表示命令执行完毕后自动删除临时容器，保持环境整洁。

## Docker 配置概览

*   `docker-compose.yml`: 项目的核心编排文件，定义了 `db`, `backend`, `storefront`, `dashboard` 四个服务以及它们之间的关系。
*   `backend/Dockerfile`: 定义了如何构建 Django 后端镜像。
*   `storefront/Dockerfile`: 定义了如何构建 Next.js 店面镜像。
*   `dashboard/Dockerfile`: 定义了如何构建 React 仪表板并使用 Nginx 托管。
*   `backend/entrypoint.sh`: 在后端容器启动时自动运行数据库迁移并启动 Gunicorn 服务器的脚本。
*   `backend/.env.docker`: 专门为 Docker 环境提供的环境变量文件。
