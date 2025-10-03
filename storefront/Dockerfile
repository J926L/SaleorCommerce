# ---- Build Stage ----
# 使用 Node.js 镜像来构建 Next.js 应用
FROM node:18-alpine AS build

WORKDIR /app

# 复制 package.json 和 package-lock.json (如果存在)
COPY package*.json ./

# 安装所有依赖
RUN npm install

# 复制所有项目文件
COPY . .

# 构建生产版本的应用
RUN npm run build

# ---- Production Stage ----
# 最终的生产镜像
FROM node:18-alpine

WORKDIR /app

# 从构建阶段复制构建好的应用和生产环境依赖
COPY --from=build /app/public ./public
COPY --from=build /app/.next ./.next
COPY --from=build /app/package.json ./

# 安装生产环境依赖
RUN npm install --production

# 暴露端口
EXPOSE 3000

# 启动 Next.js 应用
CMD ["npm", "start"]
