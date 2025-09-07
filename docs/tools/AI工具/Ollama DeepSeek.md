# Windows 下 Ollama + DeepSeek-R1-1.5B 完整部署文档

> 本文档将帮助你在 Windows 系统中从 0 到 1 完成 Ollama + DeepSeek-R1-1.5B 的安装与部署，支持在线安装与离线部署，涵盖模型目录迁移与基本使用方法。

## 📝 内容概述

本文档提供了在 Windows 系统下部署 Ollama 和 DeepSeek-R1-1.5B 模型的完整解决方案，包括在线安装、离线部署、目录迁移和实际使用等各个环节。特别适合需要在离线环境或受限网络环境中部署本地AI模型的用户。

## 🎯 核心要点

### 📋 部署目录

1. **在线安装** - Ollama + DeepSeek-R1-1.5B
2. **离线部署** - U盘携带方案
3. **目录迁移** - 模型缓存迁移到D盘
4. **使用指南** - 本地推理操作
5. **扩展功能** - 知识库问答支持（RAG）

### 1️⃣ 在线安装 Ollama + DeepSeek-R1-1.5B

#### 1.1 安装 Ollama

1. **下载安装程序**
   
   访问官网下载：`https://ollama.com/download/OllamaSetup.exe`

2. **执行安装**
   
   下载后双击安装程序完成安装。

#### 1.2 拉取 DeepSeek 模型

打开命令提示符（Win+R → 输入 `cmd`）：

```bash
ollama pull deepseek-r1:1.5b
```

模型将被下载并缓存在以下路径：
```
C:\Users\你的用户名\.ollama\models\blobs\sha256\...
```

⚠️ **注意**: 此模型体积较大，请确保有足够空间（通常 1-4GB）。

### 2️⃣ 离线部署方案（U盘迁移）

适用于目标机器无法联网的场景。

#### 2.1 在联网机器中准备资源

1. **下载 Ollama 安装包**
   
   下载地址：`https://ollama.com/download/OllamaSetup.exe`

2. **下载 DeepSeek-R1-1.5B 模型缓存**
   
   执行命令：
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

3. **复制模型缓存文件夹**
   
   - 路径：`C:\Users\你的用户名\.ollama\models`
   - 复制整个 `.ollama` 文件夹或其中的 `models` 子目录到 U 盘

#### 2.2 在离线电脑部署

1. **安装 Ollama**（双击运行安装包）
2. **初始化环境**（运行 `ollama` 命令一次后退出）
3. **复制模型文件**到相同路径：
   ```
   C:\Users\你的用户名\.ollama\models\blobs\sha256\...
   ```

### 3️⃣ 将模型目录迁移到 D 盘

#### 方法一：通过环境变量修改路径

1. **创建新目录**：
   ```
   D:\ollama\models
   ```

2. **设置环境变量**：
   - 打开「系统环境变量」设置
   - 新建用户变量：
     - 名称：`OLLAMA_MODELS`
     - 值：`D:\ollama\models`

3. **重启命令提示符**，运行：
   ```bash
   ollama run deepseek-r1:1.5b
   ```

#### 方法二：使用符号链接（软链接）

> 更适合已有 `.ollama` 文件夹内容的迁移

1. **关闭 Ollama**

2. **移动模型文件**：
   ```bash
   robocopy "C:\Users\你的用户名\.ollama" "D:\ollama" /E /MOVE
   ```

3. **创建软链接**：
   
   打开**管理员命令提示符**，执行：
   ```bash
   mklink /D "C:\Users\你的用户名\.ollama" "D:\ollama"
   ```

### 4️⃣ 使用模型进行本地推理

模型部署完成后，使用命令行运行模型：

```bash
ollama run deepseek-r1:1.5b
```

**示例对话**：
```
> 用中文介绍一下你是谁
```

模型将给出完整回答，支持中英文指令。

### 5️⃣ 离线构建知识库问答（RAG）

#### 5.1 准备依赖包（在联网机器下载）

```bash
pip download langchain chromadb sentence-transformers pypdf unstructured
```

将 `.whl` 文件拷贝至离线电脑，安装：
```bash
pip install *.whl
```

#### 5.2 示例流程

- 读取文档 → 拆分文本 → 向量化 → 存入 Chroma → Ollama 本地问答
- 使用 `langchain` 的 `ConversationalRetrievalChain` 调用 Ollama

## 💡 应用建议

### 🎯 适用场景
- **离线环境部署** - 无网络或受限网络环境
- **本地AI应用开发** - 隐私保护的本地推理
- **教学演示** - 课堂或培训环境使用
- **原型开发** - 快速验证AI应用想法

### ⚠️ 注意事项
- 确保系统有足够的存储空间（建议至少10GB可用空间）
- 离线部署时需要完整复制模型文件，避免文件损坏
- 使用软链接方法时必须以管理员权限运行
- 建议在部署前备份重要数据

### 🔧 性能优化建议
- 将模型文件存储在SSD上以提高加载速度
- 确保系统内存充足（建议8GB以上）
- 关闭不必要的后台程序以释放系统资源

### 📊 部署方法对比

| 部署方式 | 适用场景 | 难度等级 | 网络要求 | 推荐指数 |
|---------|---------|---------|---------|---------|
| 在线安装 | 有网络环境 | ⭐⭐ | 需要网络 | ⭐⭐⭐⭐⭐ |
| 离线部署 | 无网络环境 | ⭐⭐⭐ | 无需网络 | ⭐⭐⭐⭐ |
| 环境变量迁移 | 空间优化 | ⭐⭐ | 无需网络 | ⭐⭐⭐⭐⭐ |
| 软链接迁移 | 已有数据迁移 | ⭐⭐⭐⭐ | 无需网络 | ⭐⭐⭐⭐ |

## 📋 相关标签

`Ollama` `DeepSeek-R1` `Windows部署` `离线安装` `模型管理` `本地AI` `RAG` `知识库问答`

## 🔗 相关链接

- [Ollama官方文档](https://ollama.ai/docs)
- [DeepSeek模型介绍](https://deepseek.com)
- [Ollama模型迁移教程](./Ollama迁移.md)
- Windows环境变量配置指南（待补充）

---

*最后更新: 2025-01-27*
*分类: 工具辅助类*