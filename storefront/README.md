# 店面 (Saleor Commerce)

这是 Saleor Commerce 项目的店面应用程序。它是一个使用 Next.js、React 和 TypeScript 构建的现代化、高性能的前端。

## 功能特性

*   **产品展示**: 首页、产品列表页和产品详情页。
*   **购物车与结账**: 功能齐全的购物车和多步骤结账流程。
*   **客户账户**: 用户登录、注册、订单历史和地址管理。
*   **完全解耦**: 通过 GraphQL API 与后端通信。

## 技术栈

*   **框架**: Next.js, React
*   **语言**: TypeScript
*   **GraphQL 客户端**: Apollo Client
*   **样式**: Tailwind CSS

## 环境搭建

**1. 进入店面目录:**

```bash
cd SaleorCommerce/storefront
```

**2. 安装依赖:**

```bash
npm install
# 或者
yarn install
```

**3. 配置环境变量:**

*   复制 `.env.local.example` 文件为 `.env.local`。
*   更新 `NEXT_PUBLIC_API_URL` 为你的后端 GraphQL API 地址 (例如, `http://localhost:8000/graphql/`)。

**4. 运行开发服务器:**

```bash
npm run dev
# 或者
yarn dev
```

现在，店面应该运行在 `http://localhost:3000`。

## 代码风格和文档

*   遵循社区推崇的 React 和 TypeScript 最佳实践。
