> **注意:** 这是仪表板服务的独立说明。为了获得最佳体验和完整的项目设置，请优先参考项目根目录的 `README.md` 和 `DOCKER_GUIDE.md`。

# 仪表板 (Saleor Commerce)

这是 Saleor Commerce 项目的管理仪表板。它是一个使用 React 和 TypeScript 构建的单页应用程序 (SPA)，用于管理商店的各个方面。

## 技术栈

*   **框架**: React
*   **语言**: TypeScript
*   **GraphQL 客户端**: Apollo Client
*   **构建工具**: Create React App

## 本地环境搭建 (不使用 Docker)

**1. 进入仪表板目录:**

```bash
cd dashboard
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

现在，仪表板应该运行在 `http://localhost:3001`。
