# ---- Base Stage ----
# 基础镜像，包含所有构建工具
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./

# ---- Dependencies Stage ----
# 仅安装生产环境依赖
FROM base AS deps
RUN npm install --production

# ---- Build Stage ----
# 构建 Next.js 应用
FROM base AS build
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# ---- Production Stage ----
# 最终的生产镜像
FROM base AS production
ENV NODE_ENV=production

# 从构建阶段复制构建好的应用
COPY --from=build /app/public ./public
COPY --from=build /app/.next ./.next
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./

# 暴露端口
EXPOSE 3000

# 启动 Next.js 应用
CMD ["npm", "start"]
