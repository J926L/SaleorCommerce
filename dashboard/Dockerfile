# ---- Build Stage ----
# 使用 Node.js 镜像来构建 React 应用
FROM node:18-alpine AS build

WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制所有项目文件
COPY . .

# 构建生产版本的应用
RUN npm run build

# ---- Production Stage ----
# 使用 Nginx 镜像来提供静态文件
FROM nginx:1.25-alpine

# 从构建阶段复制构建好的静态文件到 Nginx 的 web 根目录
COPY --from=build /app/build /usr/share/nginx/html

# 复制 Nginx 配置文件 (如果需要自定义配置)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露 80 端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
