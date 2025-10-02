# 仪表板 (Saleor Commerce)

这是 Saleor Commerce 项目的管理仪表板。它是一个使用 React 和 TypeScript 构建的单页应用程序 (SPA)，用于管理商店的各个方面。

## 功能特性

*   **订单管理**: 查看、处理和管理订单。
*   **产品管理**: 创建、更新和管理产品、类别和集合。
*   **客户管理**: 查看和管理客户账户。
*   **商店配置**: 配置商店设置、运输方式和支付网关。

## 技术栈

*   **框架**: React
*   **语言**: TypeScript
*   **GraphQL 客户端**: Apollo Client
*   **构建工具**: Create React App

## 环境搭建

**1. 进入仪表板目录:**

```bash
cd SaleorCommerce/dashboard
```

**2. 安装依赖:**

```bash
npm install
# 或者
yarn install
```

**3. 配置环境变量:**

*   复制 `.env.local.example` 文件为 `.env.local`。
*   更新 `REACT_APP_API_URL` 为你的后端 GraphQL API 地址 (例如, `http://localhost:8000/graphql/`)。

**4. 运行开发服务器:**

```bash
npm start
# 或者
yarn start
```

现在，仪表板应该运行在 `http://localhost:3001` (或者 Create React App 指定的另一个端口)。

## 代码风格和文档

*   所有代码注释和面向用户的文本都必须使用 **简体中文**。
*   遵循社区推崇的 React 和 TypeScript 最佳实践。
