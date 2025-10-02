# Saleor Commerce: 一个功能齐全的电子商务平台

本项目是一个基于 Saleor 构建的完整、API 优先的无头电子商务平台。

## 项目结构

本项目由三个独立的部分组成：

1.  **`/backend`**: 核心 API 和业务逻辑。
    *   **技术栈**: Python, Django, Graphene (GraphQL)
    *   **数据库**: SQLite

2.  **`/storefront`**: 面向客户的店面应用程序。
    *   **技术栈**: Next.js, React, TypeScript, Apollo Client, Tailwind CSS

3.  **`/dashboard`**: 用于商店管理的仪表板应用程序。
    *   **技术栈**: React, TypeScript, Apollo Client

每个目录都包含其自己的 `README.md` 文件，其中包含详细的设置和开发说明。

## 目标

*   **API 优先**: 后端和前端通过 GraphQL API 进行通信，实现完全解耦。
*   **可扩展**: 通过插件和应用架构轻松扩展功能。

## 快速开始

请参阅每个子目录（`backend`, `storefront`, `dashboard`）中的 `README.md` 文件以获取详细的安装和启动说明。
