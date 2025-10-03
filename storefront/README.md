> **注意:** 这是店面服务的独立说明。要了解完整的项目设置选项（包括本地和 Docker），请优先参考项目根目录的 `README.md`。

# 店面 (Saleor Commerce)

这是 Saleor Commerce 项目的店面应用程序。它是一个使用 Next.js、React 和 TypeScript 构建的现代化、高性能的前端。

## 技术栈

*   **框架**: Next.js, React
*   **语言**: TypeScript
*   **GraphQL 客户端**: Apollo Client
*   **样式**: Tailwind CSS

## 本地环境搭建 (不使用 Docker)

**1. 进入店面目录:**

```bash
cd storefront
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
