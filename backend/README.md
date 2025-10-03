> **注意:** 这是后端服务的独立说明。为了获得最佳体验和完整的项目设置，请优先参考项目根目录的 `README.md` 和 `DOCKER_GUIDE.md`。

# 后端 API (Saleor Commerce)

这是 Saleor Commerce 项目的核心后端。它基于 Python、Django 和 Graphene 构建，提供了一个完整的 GraphQL API 用于电子商务功能。

## 技术栈

*   **框架**: Django
*   **API**: Graphene (GraphQL)
*   **数据库**: SQLite
*   **语言**: Python

## 本地环境搭建 (不使用 Docker)

**1. 进入后端目录:**

```bash
cd backend
```

**2. 创建并激活虚拟环境:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. 设置环境变量:**

*   将 `.env.example` 文件复制为 `.env`。
*   在 `.env` 文件中生成并填入你自己的 `SECRET_KEY`。

**4. 安装依赖:**

```bash
pip install -r requirements.txt
```

**5. 运行数据库迁移:**

```bash
python manage.py migrate
```

**6. 创建超级用户:**

```bash
python manage.py createsuperuser
```

**7. 运行开发服务器:**

```bash
python manage.py runserver
```

现在，GraphQL API 应该运行在 `http://127.0.0.1:8000/graphql/`
Django 管理后台 `http://127.0.0.1:8000/admin/`
