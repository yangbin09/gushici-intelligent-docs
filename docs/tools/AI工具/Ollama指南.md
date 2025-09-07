# Ollama 使用指南 - Windows 系统

## 📖 概述

本指南详细介绍如何在 Windows 系统上使用 Ollama 拉取和运行大语言模型。适用于已安装 Ollama 的用户，特别针对配备 NVIDIA RTX 4060 显卡的电脑进行优化说明。

## 🖥️ 系统要求

- **操作系统**: Windows 10/11
- **显卡**: NVIDIA RTX 4060（8GB 显存）
- **内存**: 建议 16GB 以上
- **存储**: 至少 20GB 可用空间（用于存储模型文件）
- **前置条件**: 已安装 Ollama

## 1️⃣ 验证 Ollama 安装

首先确认 Ollama 已正确安装：

```bash
ollama --version
```

如果显示版本信息，说明安装成功。

## 2️⃣ 拉取模型

### 2.1 查看可用模型

**查看在线模型库**：
访问 [Ollama 模型库](https://ollama.com/library) 浏览所有可用模型

**查看本地已安装模型**：
```bash
ollama list
```

**搜索在线模型**：
```bash
# 搜索包含关键词的模型（需要网络连接）
ollama search llama
ollama search mistral
```

### 2.2 推荐模型（适合 RTX 4060）

考虑到 RTX 4060 的 8GB 显存，推荐以下模型：

#### 🆕 2025年最新推荐模型

##### 阿里巴巴Qwen3系列（2025年4月发布）
Qwen3是阿里巴巴通义千问最新一代大语言模型，支持混合推理模式，在编程、数学推理等方面表现出色：

**轻量级模型（4-8GB显存）**
```bash
# Qwen3 0.6B - 超轻量级，适合边缘设备
ollama pull qwen3:0.6b

# Qwen3 4B - 性能可媲美Qwen2.5-72B-Instruct
ollama pull qwen3:4b

# Qwen3 8B - 推荐选择，平衡性能与资源消耗
ollama pull qwen3:8b
```

**中等模型（8-16GB显存）**
```bash
# Qwen3 14B - 更强的推理能力
ollama pull qwen3:14b

# Qwen3 32B - 高性能模型，支持128K上下文
ollama pull qwen3:32b
```

**大型模型（需要更多显存）**
```bash
# Qwen3 30B-A3B - MoE模型，30B总参数，3B激活参数
ollama pull qwen3:30b-a3b

# Qwen3 235B-A22B - 旗舰MoE模型，235B总参数，22B激活参数
ollama pull qwen3:235b-a22b
```

##### DeepSeek-R1系列（2025年最新版本）
DeepSeek-R1是专注推理的开源模型，性能接近OpenAI o1，支持商业使用：

**轻量级模型（2-8GB显存）**
```bash
# DeepSeek-R1 1.5B - 最小版本，2GB显卡即可运行
ollama pull deepseek-r1:1.5b

# DeepSeek-R1 7B - 基于Qwen蒸馏的高效模型
ollama pull deepseek-r1:7b

# DeepSeek-R1 8B - DeepSeek-R1-0528版本，推理能力显著提升
ollama pull deepseek-r1:8b
```

**中等模型（8-24GB显存）**
```bash
# DeepSeek-R1 14B - 适合A10等24GB显存GPU
ollama pull deepseek-r1:14b

# DeepSeek-R1 32B - 高性能推理模型
ollama pull deepseek-r1:32b
```

**大型模型（需要更多显存）**
```bash
# DeepSeek-R1 70B - 基于Llama蒸馏的大型模型
ollama pull deepseek-r1:70b

# DeepSeek-R1 671B - 完整版本，性能接近O3和Gemini 2.5 Pro
ollama pull deepseek-r1:671b
```

#### 传统推荐模型

##### 轻量级模型（4-8GB显存）
```bash
# Llama 3.2 3B - 轻量高效
ollama pull llama3.2:3b

# Qwen 2.5 7B - 中文优化
ollama pull qwen2.5:7b

# Gemma 2 9B - Google 开源模型
ollama pull gemma2:9b
```

##### 中等模型（8-12GB显存）
```bash
# Llama 3.1 8B - 平衡性能与资源消耗
ollama pull llama3.1:8b

# Qwen 2.5 14B - 更强的中文理解
ollama pull qwen2.5:14b

# Mistral 7B - 多语言支持
ollama pull mistral:7b
```

##### 大型模型（需要更多显存或CPU运行）
```bash
# Llama 3.1 70B - 高性能但需要大量资源
ollama pull llama3.1:70b

# Qwen 2.5 72B - 最强中文模型
ollama pull qwen2.5:72b

# 注意：70B+ 模型可能需要量化版本
ollama pull llama3.1:70b-instruct-q4_0
```

### 2.3 拉取示例

```bash
# 拉取 Llama 3.2 3B 模型
ollama pull llama3.2:3b
```

拉取过程中会显示下载进度：
```
pulling manifest 
pulling 8eeb52dfb3bb... 100% ▕████████████████▏ 2.0 GB                         
pulling 73b313b5552d... 100% ▕████████████████▏  1.4 KB                         
pulling 0ba8f0e314b4... 100% ▕████████████████▏  12 KB                          
pulling 56bb8bd477a5... 100% ▕████████████████▏   96 B                          
pulling 1a4c3c319823... 100% ▕████████████████▏  485 B                          
verifying sha256 digest 
writing manifest 
removing any unused layers 
success
```

## 3️⃣ 运行模型

### 3.1 启动交互式对话

```bash
# 运行 Llama 3.2 3B
ollama run llama3.2:3b
```

### 3.2 交互示例

```
>>> 你好，请介绍一下自己
你好！我是 Llama，一个由 Meta 开发的大型语言模型。我可以帮助你回答问题、进行对话、协助写作、解释概念等等。有什么我可以帮助你的吗？

>>> /bye
```

### 3.3 常用交互命令

在模型运行时，可以使用以下命令：

- `/bye` - 退出对话
- `/clear` - 清除对话历史
- `/help` - 显示帮助信息
- `/show info` - 显示模型信息
- `/show parameters` - 显示模型参数

## 4️⃣ 模型管理

### 4.1 查看已安装模型

```bash
ollama list
```

输出示例：
```
NAME                    ID              SIZE    MODIFIED
llama3.2:3b            8eeb52dfb3bb    2.0 GB  2 hours ago
phi3:mini              64c1188f2485    2.2 GB  1 day ago
mistral:7b             61e88e884507    4.1 GB  3 days ago
```

### 4.2 删除模型

```bash
# 删除指定模型
ollama rm llama3.2:3b
```

### 4.3 更新模型

```bash
# 重新拉取最新版本
ollama pull llama3.2:3b
```

## 5️⃣ 2025年新模型特点说明

### 5.1 Qwen3系列特点
- **混合推理模式**：支持快速模式和深度思考模式
- **长上下文支持**：支持128K上下文长度，适合处理长文档
- **多语言优化**：在中文、英文等多种语言上表现优秀
- **专业领域**：在编程、数学、科学推理等领域性能突出
- **MoE架构**：大型模型采用专家混合架构，提高效率

### 5.2 DeepSeek-R1系列特点
- **推理专精**：专门针对复杂推理任务优化
- **商业友好**：支持商业使用，无限制
- **多版本选择**：从1.5B到671B多种参数规模
- **蒸馏技术**：小参数模型通过蒸馏技术保持高性能
- **思维链推理**：内置思维链推理能力，逻辑性强

### 5.3 RTX 4060用户推荐配置
**最佳选择（8GB显存）**：
- `qwen3:8b` - 综合性能最佳
- `deepseek-r1:7b` - 推理任务首选
- `deepseek-r1:8b` - 最新版本，推理能力更强

**轻量选择（节省显存）**：
- `qwen3:4b` - 性能接近大模型
- `deepseek-r1:1.5b` - 最小资源消耗

## 6️⃣ 性能优化建议

### 6.1 针对 RTX 4060 的优化

1. **选择合适的模型大小**
   - 3B-7B 参数的模型最适合
   - 避免同时运行多个大模型

2. **监控显存使用**
   ```bash
   # 使用 nvidia-smi 监控显存
   nvidia-smi
   ```

3. **调整模型参数**
   ```bash
   # 运行时指定参数
   ollama run llama3.2:3b --num-gpu 1
   ```

### 6.2 系统优化

1. **关闭不必要的程序**，释放内存和显存
2. **确保充足的存储空间**，模型文件较大
3. **保持系统更新**，包括显卡驱动

## 7️⃣ 常见问题解决

### 7.1 显存不足

**问题**: 运行大模型时显存不足
**解决方案**:
- 选择更小的模型（如 3B 而非 7B）
- 使用量化版本（如 q4_0, q8_0）
- 关闭其他占用显存的程序

### 7.2 下载速度慢

**问题**: 模型下载速度很慢
**解决方案**:
- 检查网络连接
- 尝试使用代理
- 选择合适的下载时间

### 7.3 模型无法启动

**问题**: 模型拉取成功但无法运行
**解决方案**:
```bash
# 检查模型完整性
ollama show llama3.2:3b

# 重新拉取模型
ollama pull llama3.2:3b
```

## 8️⃣ 高级用法

### 8.1 API 调用

Ollama 提供 REST API 接口：

```bash
# 启动 Ollama 服务
ollama serve
```

然后可以通过 HTTP 请求调用：

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:3b",
  "prompt": "为什么天空是蓝色的？"
}'
```

### 8.2 自定义模型

可以基于现有模型创建自定义版本：

```bash
# 创建 Modelfile
echo 'FROM llama3.2:3b
SYSTEM "你是一个专业的编程助手"' > Modelfile

# 构建自定义模型
ollama create my-coding-assistant -f Modelfile
```

## 9️⃣ 总结

使用 Ollama 在 Windows 系统上运行大语言模型的基本流程：

1. **验证安装**: `ollama --version`
2. **拉取模型**: `ollama pull model-name`
3. **运行模型**: `ollama run model-name`
4. **管理模型**: `ollama list`, `ollama rm`

对于 RTX 4060 用户，建议从 3B-7B 参数的模型开始，根据实际性能表现调整选择。

::: tip 💡 推荐配置
对于RTX 4060用户，我们特别推荐：
- **新手**: `qwen3:4b` 或 `deepseek-r1:1.5b`
- **进阶**: `qwen3:8b` 或 `deepseek-r1:8b`
- **专业**: `qwen3:14b`（需要更多显存）
:::

::: warning ⚠️ 注意事项
- 大型模型（70B+）可能需要CPU运行，速度较慢
- 确保有足够的存储空间，模型文件通常几GB到几十GB
- 首次下载模型需要良好的网络连接
:::

## 🔗 相关资源

- [Ollama 官网](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [模型库](https://ollama.com/library)
- [社区讨论](https://github.com/ollama/ollama/discussions)

---

*最后更新: 2024年12月*