---
title: 'Dyad AI应用构建工具使用指南'
description: '免费开源的本地AI应用构建工具，支持全栈开发、多模型集成和一键部署'
tags: [AI工具, 应用开发, 全栈开发, 本地部署, 开源工具]
category: '工具辅助类'
difficulty: 3
recommended: 4
created: '2025-01-15'
---

# {{ $frontmatter.title }}

## 📝 概述

{{ $frontmatter.description }}

Dyad是一个革命性的AI应用构建平台，让你通过自然语言对话即可创建全栈应用。<mcreference link="https://www.dyad.sh/?utm_source=chatgpt.com" index="0">0</mcreference> 与传统应用构建工具不同，Dyad提供完全的代码控制权，支持多种AI模型，并且完全开源。<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>

## 🚀 核心特性

### 🔓 零锁定策略

- **本地代码控制**: 所有源码保存在本地，完全掌控<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **自由导出**: 支持React前端、无服务器后端完整导出
- **IDE集成**: 无缝对接VS Code、Cursor等主流编辑器<mcreference link="https://www.dyad.sh/?utm_source=chatgpt.com" index="0">0</mcreference>

### 🤖 多模型支持

- **主流AI模型**: OpenAI GPT-4.1、Claude Sonnet 4、Google Gemini 2.5 Pro<mcreference link="https://www.dyad.sh/?utm_source=chatgpt.com" index="0">0</mcreference>
- **本地模型**: 支持Ollama等本地LLM部署
- **自带API密钥**: 使用自己的API密钥，无额外费用<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>

### 🏗️ 全栈开发能力

- **Supabase集成**: 内置用户认证、数据库、服务器函数<mcreference link="https://www.dyad.sh/?utm_source=chatgpt.com" index="0">0</mcreference>
- **自动版本控制**: 基于Git的自动版本管理，支持即时撤销<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **实时预览**: 代码生成后立即预览运行效果

## 📋 安装与配置

### 1. 系统要求

- **支持平台**: macOS 12+、Windows 10/11 64位<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **内存要求**: 推荐4GB+RAM
- **网络要求**: 仅远程AI模型需要网络连接

### 2. 下载安装

1. **获取安装包**: 访问[官网](https://www.dyad.sh/)下载，无需注册账户<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
2. **Windows安全提示**: 首次运行会显示蓝色警告，点击"更多信息"→"仍要运行"<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
3. **开源验证**: 所有源码公开可查，确保安全性

### 3. 环境配置

#### Node.js安装

- **必需组件**: 安装Node.js作为JavaScript运行时<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
- **安装指导**: 应用内提供详细安装指引
- **故障排除**: 遇到问题可查看node.js帮助页面

#### AI模型配置

- **推荐选择**: Google Gemini API密钥（每日250条免费额度）<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
- **多模型支持**: 可同时配置多个AI服务
- **本地模型**: 支持Ollama等完全离线方案

## 🛠️ 使用流程

### 第一个应用创建

1. **需求描述**: 在聊天框输入功能需求（如"创建待办事项应用"）<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
2. **代码生成**: AI自动生成完整的应用代码框架
3. **审核确认**: 检查生成的代码并确认应用<mcreference link="https://www.dyad.sh/docs/getting-started/quickstart?utm_source=chatgpt.com" index="1">1</mcreference>
4. **实时预览**: 右侧窗口显示应用运行效果

### 迭代开发

- **功能扩展**: 继续对话添加新功能（如"添加暗色模式"）
- **代码修改**: 使用本地编辑器进行精细调整
- **版本管理**: 每次修改自动保存为Git提交

## 🚀 部署发布

### GitHub集成

1. **项目连接**: 在应用详情页点击"Connect to GitHub"<mcreference link="https://www.dyad.sh/docs/getting-started/publishing-your-app?utm_source=chatgpt.com" index="3">3</mcreference>
2. **授权设置**: 授权Dyad访问GitHub仓库
3. **代码同步**: 点击"Sync to GitHub"推送代码<mcreference link="https://www.dyad.sh/docs/getting-started/publishing-your-app?utm_source=chatgpt.com" index="3">3</mcreference>

### Vercel部署

1. **平台选择**: 推荐使用Vercel的免费计划<mcreference link="https://www.dyad.sh/docs/getting-started/publishing-your-app?utm_source=chatgpt.com" index="3">3</mcreference>
2. **GitHub登录**: 使用GitHub账户登录Vercel
3. **项目导入**: 在Vercel导入GitHub项目<mcreference link="https://www.dyad.sh/docs/getting-started/publishing-your-app?utm_source=chatgpt.com" index="3">3</mcreference>
4. **自动部署**: Vercel自动识别框架并部署
5. **访问地址**: 获得类似`your-app.vercel.app`的公网地址<mcreference link="https://www.dyad.sh/docs/getting-started/publishing-your-app?utm_source=chatgpt.com" index="3">3</mcreference>

### 持续部署

- **自动更新**: 每次GitHub同步触发Vercel重新部署
- **环境变量**: 如需API集成，在Vercel配置环境变量
- **安全提醒**: 确保应用有适当的认证和安全保护

## 🎯 高级技巧

### 大型应用管理

#### 长上下文模型

- **推荐模型**: Google Gemini支持100万token上下文<mcreference link="https://www.dyad.sh/docs/guides/large-apps?utm_source=chatgpt.com" index="4">4</mcreference>
- **性能优势**: 在长上下文基准测试中表现优异

#### 智能上下文管理

- **Pro功能**: Smart Context自动选择相关文件<mcreference link="https://www.dyad.sh/docs/guides/large-apps?utm_source=chatgpt.com" index="4">4</mcreference>
- **Token压缩**: 使用小模型预选文件，有效处理超百万token
- **适用场景**: 避免"让应用更好"等宽泛查询

#### 手动上下文控制

- **Glob路径**: 使用`src/**`、`dir/*.ts`等模式指定文件<mcreference link="https://www.dyad.sh/docs/guides/large-apps?utm_source=chatgpt.com" index="4">4</mcreference>
- **Pro增强**: 自动包含关键模块，指导Smart Context选择
- **注意事项**: 可能导致代码重复或新文件创建

### 应用拆分策略

#### 用户类型分离

- **管理后台**: 独立的管理员应用
- **用户前端**: 面向普通用户的应用界面

#### 功能模块分离

- **营销站点**: 独立的落地页和宣传页面<mcreference link="https://www.dyad.sh/docs/guides/large-apps?utm_source=chatgpt.com" index="4">4</mcreference>
- **子域部署**: 如`app.yoursite.com`和`yoursite.com`
- **模块化设计**: 按功能目录组织，便于维护

## 📊 性能数据

### 社区指标

- **GitHub星标**: 7,200+ stars，749+ forks<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **用户下载**: 100,000+次下载
- **用户评分**: 4.9/5分用户满意度<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **开发效率**: 相比云端构建工具，bug减少50%，迭代速度提升2倍

### 技术规格

- **主要语言**: TypeScript (96.9%)<mcreference link="https://www.oneclickitsolution.com/centerofexcellence/aiml/dyad-open-source-ai-app-builder?utm_source=chatgpt.com" index="2">2</mcreference>
- **开源协议**: Apache-2.0许可证
- **应用类型**: 全栈应用（前端+后端+数据库）
- **部署方式**: 支持任意云平台部署

## 💡 使用建议

### 最佳实践

1. **从简单开始**: 先创建基础功能，逐步迭代
2. **模块化思维**: 将复杂应用拆分为独立模块
3. **版本控制**: 充分利用自动Git管理功能
4. **本地编辑**: 结合专业IDE进行精细开发

### 注意事项

- **网络安全**: 部署前确保应用有适当的安全措施
- **API配额**: 注意AI模型的使用限制和费用
- **备份策略**: 虽然有版本控制，建议定期备份重要项目

::: tip 开发提示

- 使用具体明确的需求描述，避免过于宽泛的指令
- 对于大型项目，考虑使用Pro版本的Smart Context功能
- 充分利用Supabase集成，快速构建后端功能
- 定期同步到GitHub，确保代码安全
  :::

## 🔗 相关资源

- [Dyad官网](https://www.dyad.sh/)
- [快速开始指南](https://www.dyad.sh/docs/getting-started/quickstart)
- [应用发布教程](https://www.dyad.sh/docs/getting-started/publishing-your-app)
- [大型应用构建指南](https://www.dyad.sh/docs/guides/large-apps)
- [GitHub仓库](https://github.com/dyad-sh/dyad)
- [社区论坛](https://reddit.com/r/dyad)

---

_最后更新: 2025-01-15_  
_难度等级: ⭐⭐⭐ (中等)_  
_推荐指数: ⭐⭐⭐⭐ (推荐)_
