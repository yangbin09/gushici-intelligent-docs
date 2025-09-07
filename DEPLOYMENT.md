# 部署配置说明

## GitHub Secrets 配置

为了使用SSH部署到远程服务器，需要在GitHub仓库的Settings > Secrets and variables > Actions中配置以下环境变量：

### 必需的Secrets

| Secret名称 | 描述 | 示例值 |
|-----------|------|--------|
| `SSH_HOSTNAME` | 服务器IP地址或域名 | `192.168.1.100` 或 `example.com` |
| `SSH_USERNAME` | SSH登录用户名 | `root` 或 `ubuntu` |
| `SSH_PASSWORD` | SSH登录密码 | `your_password` |
| `SSH_PORT` | SSH端口号 | `22` |
| `REMOTE_WEB_DIR` | 网站文件部署目录 | `/var/www/html` |
| `REMOTE_BACKUP_DIR` | 备份文件存储目录 | `/var/backups/website` |

### 可选的Secrets

| Secret名称 | 描述 | 默认值 | 示例值 |
|-----------|------|--------|--------|
| `ENABLE_GZIP` | 是否启用Gzip压缩 | `false` | `true` |

## 服务器环境要求

### 系统要求
- Linux系统（Ubuntu/CentOS/Debian等）
- Nginx Web服务器
- 具有sudo权限的用户账户

### 目录权限
确保部署目录具有正确的权限：
```bash
# 创建网站目录
sudo mkdir -p /var/www/html
sudo mkdir -p /var/backups/website

# 设置权限
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

### Nginx配置示例

创建或编辑Nginx配置文件 `/etc/nginx/sites-available/default`：

```nginx
server {
    listen 80;
    server_name your_domain.com;
    root /var/www/html;
    index index.html;

    # Gzip压缩配置
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;

    # 静态文件缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # SPA路由支持
    location / {
        try_files $uri $uri/ /index.html;
    }

    # 安全头
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

启用配置并重启Nginx：
```bash
sudo nginx -t
sudo systemctl reload nginx
```

## 部署流程

1. **代码推送**：当代码推送到`main`或`master`分支时，自动触发部署
2. **构建**：使用VitePress构建静态网站
3. **备份**：在部署前备份当前网站文件
4. **部署**：将构建好的文件传输到服务器
5. **配置**：设置文件权限并重新加载Nginx
6. **验证**：检查网站状态

## 安全建议

1. **使用SSH密钥**：建议使用SSH密钥而不是密码进行认证
2. **限制SSH访问**：配置防火墙只允许必要的IP访问SSH端口
3. **定期更新**：保持服务器系统和软件包的更新
4. **监控日志**：定期检查Nginx和系统日志

## 故障排除

### 常见问题

1. **SSH连接失败**
   - 检查服务器IP、端口、用户名和密码
   - 确认服务器SSH服务正在运行
   - 检查防火墙设置

2. **文件权限错误**
   - 确保部署目录存在且有正确权限
   - 检查www-data用户是否存在

3. **Nginx配置错误**
   - 使用`nginx -t`测试配置文件语法
   - 检查Nginx错误日志：`sudo tail -f /var/log/nginx/error.log`

4. **网站无法访问**
   - 检查Nginx状态：`sudo systemctl status nginx`
   - 确认防火墙允许HTTP/HTTPS流量
   - 检查域名DNS解析

### 日志查看

```bash
# 查看部署日志（在GitHub Actions中）
# 查看Nginx访问日志
sudo tail -f /var/log/nginx/access.log

# 查看Nginx错误日志
sudo tail -f /var/log/nginx/error.log

# 查看系统日志
sudo journalctl -u nginx -f
```