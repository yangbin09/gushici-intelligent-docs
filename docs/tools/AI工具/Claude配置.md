# Claude Desktop 配置指南

本指南将帮助您配置 Claude Desktop 应用，以便更好地使用 AI 写作功能。

## 📋 配置要求

- Claude Desktop 应用
- 有效的 Anthropic API 密钥
- 基本的 JSON 配置知识

## ⚙️ 配置步骤

### 1. 安装 Claude Desktop

首先从官方网站下载并安装 Claude Desktop 应用。

### 2. 获取 API 密钥

1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 创建账户或登录现有账户
3. 生成新的 API 密钥
4. 妥善保存密钥（请勿泄露）

### 3. 配置文件设置

在项目根目录中，您可以找到 `claude_desktop_config_example.json` 配置示例文件。

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-brave-api-key"
      }
    }
  }
}
```

### 4. 环境变量设置

确保设置以下环境变量：

- `ANTHROPIC_API_KEY`: 您的 Anthropic API 密钥
- `BRAVE_API_KEY`: Brave 搜索 API 密钥（可选）

## 🔧 高级配置

### MCP 服务器配置

Model Context Protocol (MCP) 服务器可以扩展 Claude 的功能：

- **文件系统访问**: 允许 Claude 读取和写入本地文件
- **网络搜索**: 集成搜索引擎功能
- **自定义工具**: 添加特定领域的工具和功能

### 安全注意事项

1. **API 密钥安全**: 永远不要在代码中硬编码 API 密钥
2. **文件访问权限**: 仅授予必要的文件系统访问权限
3. **网络访问**: 谨慎配置网络相关的 MCP 服务器

## 🚀 使用技巧

### 1. 优化提示词

- 使用清晰、具体的指令
- 提供足够的上下文信息
- 分步骤描述复杂任务

### 2. 文件管理

- 保持项目文件结构清晰
- 使用有意义的文件名
- 定期备份重要配置

### 3. 性能优化

- 合理设置请求频率限制
- 避免过大的文件操作
- 监控 API 使用量

## 🔍 故障排除

### 常见问题

**问题**: Claude Desktop 无法连接
- 检查网络连接
- 验证 API 密钥是否正确
- 确认配置文件格式正确

**问题**: MCP 服务器启动失败
- 检查依赖是否安装完整
- 验证环境变量设置
- 查看错误日志信息

**问题**: 文件访问权限错误
- 确认文件路径正确
- 检查文件系统权限
- 验证 MCP 服务器配置

## 📚 相关资源

- [Anthropic 官方文档](https://docs.anthropic.com/)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [Claude Desktop 用户指南](https://claude.ai/desktop)

---

💡 **提示**: 配置完成后，建议先进行简单测试，确保所有功能正常工作后再进行复杂操作。