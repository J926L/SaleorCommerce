# Saleor Commerce: 一个功能齐全的电子商务平台

本项目是一个基于 Saleor 构建的完整、API 优先的无头电子商务平台。

## 快速开始

我们提供两种方式来运行本项目：**本地手动运行 (推荐)** 或 **使用 Docker**。

### 1. 本地开发 (推荐)

这是当前推荐的运行方式。你需要手动在你的机器上分别运行每个服务。

你需要打开三个独立的终端窗口，然后按照每个子目录中的 `README.md` 文件进行设置和启动：

*   **启动后端服务**: 进入 `backend/` 目录并遵循其 `README.md` 指引。
*   **启动店面服务**: 进入 `storefront/` 目录并遵循其 `README.md` 指引。
*   **启动仪表板服务**: 进入 `dashboard/` 目录并遵循其 `README.md` 指引。

当所有服务都成功启动后，你就可以在浏览器中访问项目的各个部分了：

*   **店面 (Storefront)**: `http://localhost:3000`
*   **仪表板 (Dashboard)**: `http://localhost:3001`
*   **后端 API (Backend)**: `http://localhost:8000/graphql/`

### 2. 使用 Docker (未测试)

本项目包含一套完整的 Docker 配置，理论上可以一键启动所有服务。但请注意，此配置**尚未经过充分测试**，可能存在问题。

如果你希望尝试，详细步骤请参阅 **[DOCKER_GUIDE.md](./DOCKER_GUIDE.md)** 文件。

## 项目结构

本项目由三个独立的部分组成：

1.  **`/backend`**: 核心 API 和业务逻辑。
    *   **技术栈**: Python, Django, Graphene (GraphQL)
    *   **数据库**: SQLite (本地开发) / PostgreSQL (Docker)

2.  **`/storefront`**: 面向客户的店面应用程序。
    *   **技术栈**: Next.js, React, TypeScript, Apollo Client, Tailwind CSS

3.  **`/dashboard`**: 用于商店管理的仪表板应用程序。
    *   **技术栈**: React, TypeScript, Apollo Client

## 目标

*   **API 优先**: 后端和前端通过 GraphQL API 进行通信，实现完全解耦。
*   **可扩展**: 通过插件和应用架构轻松扩展功能。
