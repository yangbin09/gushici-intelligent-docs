# 服务器工具 🖥️

这里收集了各种服务器配置、运维和管理相关的工具和指南，帮助你更好地管理和优化服务器环境。

## 🖥️ 操作系统安装

### [CentOS Stream 9安装指南](./CentOS Stream 9安装指南.md)

完整的CentOS Stream 9系统安装教程：

- 💿 镜像文件下载和选择指南
- ⚙️ VMware虚拟机环境配置
- 🔧 系统安装详细步骤说明
- 🌐 网络配置和连接设置
- 🔐 用户权限和安全配置
- 📋 安装后的系统优化建议

## 🌐 Web服务器

### [Nginx基础知识详解](./Nginx基础指南.md)

高性能Web服务器核心概念与实践：

- 🏗️ Nginx架构原理和工作机制
- ⚙️ 配置文件详解和最佳实践
- ⚖️ 负载均衡和反向代理配置
- 🚀 性能优化和故障排查
- 🔒 安全配置和访问控制
- 📊 监控和日志管理

## 🎯 服务器工具分类

### 操作系统

| 系统            | 特点               | 适用场景             | 学习难度 |
| --------------- | ------------------ | -------------------- | -------- |
| CentOS Stream 9 | 稳定、企业级       | 生产服务器、企业应用 | ⭐⭐⭐   |
| Ubuntu Server   | 易用、社区支持好   | 开发环境、云服务器   | ⭐⭐     |
| RHEL            | 商业支持、高稳定性 | 关键业务系统         | ⭐⭐⭐⭐ |

### Web服务器

| 工具   | 特点                | 适用场景           | 学习难度 |
| ------ | ------------------- | ------------------ | -------- |
| Nginx  | 高性能、低内存      | 高并发、反向代理   | ⭐⭐⭐   |
| Apache | 功能丰富、模块化    | 传统Web服务        | ⭐⭐⭐⭐ |
| Caddy  | 自动HTTPS、简单配置 | 小型项目、快速部署 | ⭐⭐     |

### 负载均衡

| 工具       | 类型         | 特点       | 适用场景   |
| ---------- | ------------ | ---------- | ---------- |
| Nginx      | 软件负载均衡 | 轻量、高效 | 中小型应用 |
| HAProxy    | 专业负载均衡 | 功能强大   | 大型应用   |
| Cloudflare | CDN负载均衡  | 全球分布   | 全球化应用 |

## 🚀 快速部署指南

### Nginx基础配置

```nginx
# 基础Web服务器配置
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### 反向代理配置

```nginx
# API反向代理
location /api/ {
    proxy_pass http://localhost:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

### 负载均衡配置

```nginx
# 负载均衡配置
upstream backend {
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;
    server 192.168.1.12:8080;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

## 🔧 高级配置

### SSL/HTTPS配置

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
}
```

### 缓存配置

```nginx
# 静态资源缓存
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# 代理缓存
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;

location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 1h;
    proxy_pass http://backend;
}
```

### 安全配置

```nginx
# 安全头设置
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header X-Content-Type-Options "nosniff" always;

# 限制请求频率
limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;

location /login {
    limit_req zone=login burst=5;
    proxy_pass http://backend;
}
```

## 📊 性能优化

### 系统级优化

1. **内核参数调优**

   ```bash
   # 增加文件描述符限制
   ulimit -n 65535

   # 调整TCP参数
   echo 'net.core.somaxconn = 65535' >> /etc/sysctl.conf
   ```

2. **Nginx工作进程优化**

   ```nginx
   # 设置工作进程数为CPU核心数
   worker_processes auto;

   # 每个进程的最大连接数
   events {
       worker_connections 1024;
       use epoll;
   }
   ```

### 应用级优化

1. **启用Gzip压缩**

   ```nginx
   gzip on;
   gzip_vary on;
   gzip_min_length 1024;
   gzip_types text/plain text/css application/json application/javascript;
   ```

2. **开启Sendfile**
   ```nginx
   sendfile on;
   tcp_nopush on;
   tcp_nodelay on;
   ```

## 🔍 监控和维护

### 日志管理

```nginx
# 访问日志格式
log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                '$status $body_bytes_sent "$http_referer" '
                '"$http_user_agent" "$http_x_forwarded_for"';

access_log /var/log/nginx/access.log main;
error_log /var/log/nginx/error.log warn;
```

### 状态监控

```nginx
# 启用状态页面
location /nginx_status {
    stub_status on;
    access_log off;
    allow 127.0.0.1;
    deny all;
}
```

### 健康检查

```bash
# 检查Nginx配置
nginx -t

# 重新加载配置
nginx -s reload

# 查看进程状态
ps aux | grep nginx
```

## 🛠️ 故障排除

### 常见问题

1. **502 Bad Gateway**
   - 后端服务未启动
   - 防火墙阻止连接
   - 超时设置过短

2. **403 Forbidden**
   - 文件权限问题
   - 目录索引被禁用
   - SELinux策略限制

3. **504 Gateway Timeout**
   - 后端响应时间过长
   - 代理超时设置过短
   - 网络连接问题

### 调试技巧

1. **查看错误日志**

   ```bash
   tail -f /var/log/nginx/error.log
   ```

2. **测试配置文件**

   ```bash
   nginx -t -c /etc/nginx/nginx.conf
   ```

3. **检查端口占用**
   ```bash
   netstat -tlnp | grep :80
   ```

## 📚 学习资源

### 官方文档

- [Nginx官方文档](https://nginx.org/en/docs/)
- [Nginx配置示例](https://www.nginx.com/resources/wiki/)

### 实用工具

- [Nginx配置生成器](https://nginxconfig.io/)
- [SSL配置测试](https://www.ssllabs.com/ssltest/)
- [性能测试工具](https://httpd.apache.org/docs/2.4/programs/ab.html)

### 社区资源

- [Nginx中文文档](https://nginx.org/cn/docs/)
- [运维社区](https://www.ops-coffee.cn/)

## 🎉 实际应用案例

### 静态网站托管

- 个人博客部署
- 企业官网托管
- 文档网站发布

### API网关

- 微服务架构
- API版本管理
- 请求路由分发

### 负载均衡

- 高可用架构
- 流量分发
- 故障转移

### CDN加速

- 静态资源加速
- 全球内容分发
- 缓存优化

::: tip 💡 运维提示
服务器配置需要根据实际业务需求进行调优，建议在测试环境充分验证后再应用到生产环境。
:::

::: warning ⚠️ 安全提醒
服务器安全配置至关重要，包括防火墙设置、SSL证书配置、访问控制等，务必重视安全防护。
:::
