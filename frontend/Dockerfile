FROM node:24-slim AS stage1
WORKDIR /app
COPY package-lock.json package.json /app/
RUN npm ci
COPY src /app/src
COPY index.html vite.config.js /app/
RUN npm run build

FROM nginx:1.30.6-alpine
COPY --from=stage1 /app/dist /usr/share/nginx/html
COPY default.conf  /etc/nginx/conf.d/default.conf