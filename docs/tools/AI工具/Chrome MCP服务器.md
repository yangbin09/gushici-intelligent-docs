---
title: "Chrome MCP Server - 浏览器AI自动化工具"
description: "基于Chrome扩展的模型上下文协议服务器，让AI接管你的浏览器，实现复杂的浏览器自动化、内容分析和语义搜索"
tags: [Chrome, MCP, 浏览器自动化, AI工具, 扩展]
category: "工具辅助类"
difficulty: 4
recommended: 5
created: "2025-01-15"
---

# Chrome MCP Server 🚀

## 📝 概述

**Chrome MCP Server** 是一个基于Chrome扩展的模型上下文协议(MCP)服务器，它将您的Chrome浏览器功能暴露给Claude等AI助手，实现复杂的浏览器自动化、内容分析和语义搜索等。与传统的浏览器自动化工具（如playwright）不同，Chrome MCP server直接使用您日常使用的chrome浏览器，基于现有的用户习惯和配置、登录态，让各种大模型或者各种chatbot都可以接管你的浏览器，真正成为你的日常助手。

**许可证**: MIT | **语言**: TypeScript | **类型**: Chrome扩展

## ✨ 核心特性

- 😁 **chatbot/模型无关**: 让任意你喜欢的llm或chatbot客户端或agent来自动化操作你的浏览器
- ⭐️ **使用你原本的浏览器**: 无缝集成用户本身的浏览器环境（你的配置、登录态等）
- 💻 **完全本地运行**: 纯本地运行的mcp server，保证用户隐私
- 🚄 **Streamable http**: Streamable http的连接方式
- 🏎 **跨标签页**: 跨标签页的上下文
- 🧠 **语义搜索**: 内置向量数据库和本地小模型，智能发现浏览器标签页内容
- 🔍 **智能内容分析**: AI驱动的文本提取和相似度匹配
- 🌐 **20+工具**: 支持截图、网络监控、交互操作、书签管理、浏览历史等20多种工具
- 🚀 **SIMD加速AI**: 自定义WebAssembly SIMD优化，向量运算速度提升4-8倍

## 🆚 与同类项目对比

| 对比维度 | 基于Playwright的MCP Server | 基于Chrome插件的MCP Server |
|----------|---------------------------|---------------------------|
| 资源占用 | ❌ 需启动独立浏览器进程，需要安装Playwright依赖，下载浏览器二进制等 | ✅ 无需启动独立的浏览器进程，直接利用用户已打开的Chrome浏览器 |
| 用户会话复用 | ❌ 需重新登录 | ✅ 自动使用已登录状态 |
| 浏览器环境保持 | ❌ 干净环境缺少用户设置 | ✅ 完整保留用户环境 |
| API访问权限 | ⚠️ 受限于Playwright API | ✅ Chrome原生API全访问 |
| 启动速度 | ❌ 需启动浏览器进程 | ✅ 只需激活插件 |
| 响应速度 | 50-200ms进程间通信 | ✅ 更快 |

## 🚀 快速开始

### 环境要求

- Node.js >= 18.19.0 和（npm 或 pnpm）
- Chrome/Chromium 浏览器

### 安装步骤

#### 1. 下载Chrome扩展

从GitHub上下载最新的chrome扩展：

**下载地址**: `https://github.com/hangwin/mcp-chrome/releases`

#### 2. 全局安装mcp-chrome-bridge

**使用npm**:
```bash
npm install -g mcp-chrome-bridge
```

**使用pnpm**:
```bash
# 方法1：全局启用脚本（推荐）
pnpm config set enable-pre-post-scripts true
pnpm install -g mcp-chrome-bridge

# 方法2：如果postinstall没有运行，手动注册
pnpm install -g mcp-chrome-bridge
mcp-chrome-bridge register
```

::: warning 注意
pnpm v7+ 默认禁用postinstall脚本以提高安全性。enable-pre-post-scripts设置控制是否运行pre/post安装脚本。如果自动注册失败，请使用上述手动注册命令。
:::

#### 3. 加载Chrome扩展

1. 打开Chrome并访问 `chrome://extensions/`
2. 启用"开发者模式"
3. 点击"加载已解压的扩展程序"，选择下载的扩展文件夹
4. 点击插件图标打开插件，点击连接即可看到mcp的配置

### 在支持MCP协议的客户端中使用

#### 使用streamable http的方式连接（👍🏻推荐）

将以下配置添加到客户端的MCP配置中，以cherryStudio为例：

```json
{
  "mcpServers": {
    "chrome-mcp-server": {
      "type": "streamableHttp",
      "url": "http://127.0.0.1:12306/mcp"
    }
  }
}
```

#### 使用stdio的方式连接（备选）

如果你的客户端仅支持stdio的连接方式，请使用下面的方法：

1. **查看npm包安装位置**:
```bash
# npm 查看方式
npm list -g mcp-chrome-bridge
# pnpm 查看方式
pnpm list -g mcp-chrome-bridge
```

2. **配置路径**:
假设上面的命令输出的路径是：`/Users/xxx/Library/pnpm/global/5`
那么你的最终路径就是：`/Users/xxx/Library/pnpm/global/5/node_modules/mcp-chrome-bridge/dist/mcp/mcp-server-stdio.js`

3. **添加配置**:
```json
{
  "mcpServers": {
    "chrome-mcp-stdio": {
      "command": "npx",
      "args": [
        "node",
        "/Users/xxx/Library/pnpm/global/5/node_modules/mcp-chrome-bridge/dist/mcp/mcp-server-stdio.js"
      ]
    }
  }
}
```

## 🛠️ 可用工具

### 📊 浏览器管理 (6个工具)
- 标签页管理
- 窗口控制
- 导航操作
- 页面刷新
- 历史记录
- 书签管理

### 📸 截图和视觉 (1个工具)
- 全页面截图
- 元素截图
- 可视区域截图

### 🌐 网络监控 (4个工具)
- 网络请求捕获
- 响应分析
- 性能监控
- 资源加载

### 🔍 内容分析 (4个工具)
- 文本提取
- 语义搜索
- 内容相似度
- 智能匹配

### 🎯 交互操作 (3个工具)
- 点击操作
- 表单填写
- 键盘输入

### 📚 数据管理 (5个工具)
- 数据导出
- 配置管理
- 缓存控制
- 存储操作
- 同步功能

## 🧪 使用示例

### AI帮你总结网页内容然后自动控制excalidraw画图

**指令**: 帮我总结当前页面内容，然后画个图帮我理解

### AI先分析图片的内容元素，然后再自动控制excalidraw把图片模仿出来

**指令**: 先看下图片是否能用excalidraw画出来，如果则列出所需的步骤和元素，然后画出来

### AI自动帮你注入脚本并修改网页的样式

**指令**: 帮我修改当前页面的样式，去掉广告

### AI自动帮你捕获网络请求

**指令**: 我想知道小红书的搜索接口是哪个，响应体结构是什么样的

### AI帮你分析你的浏览记录

**指令**: 分析一下我近一个月的浏览记录

### 网页对话

**指令**: 翻译并总结当前网页

### AI帮你自动截图

**网页截图指令**: 把huggingface的首页截个图
**元素截图指令**: 把huggingface首页的图标截取下来

### AI帮你管理书签

**指令**: 将当前页面添加到书签中，放到合适的文件夹

### 自动关闭网页

**指令**: 关闭所有shadcn相关的网页

## 🚧 未来发展路线图

我们对Chrome MCP Server的未来发展有着激动人心的计划：

- ✅ 身份认证
- ✅ 录制与回放
- ✅ 工作流自动化
- ✅ 增强浏览器支持（Firefox扩展）

## 🤝 贡献指南

我们欢迎贡献！请查看项目的CONTRIBUTING文档了解详细指南。

## 📄 许可证

本项目采用MIT许可证 - 详见LICENSE文件。

## 🔗 相关资源

- [GitHub仓库](https://github.com/hangwin/mcp-chrome)
- [完整工具列表](https://github.com/hangwin/mcp-chrome/blob/main/docs/tools.md)
- [架构设计文档](https://github.com/hangwin/mcp-chrome/blob/main/docs/architecture.md)
- [故障排除指南](https://github.com/hangwin/mcp-chrome/blob/main/docs/troubleshooting.md)

::: tip 💡 使用技巧
1. 建议使用streamable http连接方式，性能更好
2. 确保Chrome扩展已正确加载并连接
3. 定期更新扩展和bridge包以获得最新功能
4. 遇到问题时可查看浏览器控制台日志
:::

::: warning ⚠️ 注意事项
- 项目仍处于早期阶段，正在紧锣密鼓开发中
- 后续将有更多新功能，以及稳定性等的提升
- 如遇bug，请在GitHub上提交issue
- 确保浏览器版本兼容性
:::