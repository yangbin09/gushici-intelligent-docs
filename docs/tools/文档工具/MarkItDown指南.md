# MarkItDown-MCP 使用说明

## 📖 概述

MarkItDown-MCP 是一个强大的文档格式转换工具，可以将各种文档格式（PDF、Word、Excel、PowerPoint、图片、音频、视频等）转换为 Markdown 格式。本工具特别适合与 Claude Desktop 集成使用。

## ✅ 安装状态

**MarkItDown-MCP 已成功安装！**

- **版本**: 0.0.1a4
- **Python 路径**: `C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe`
- **安装位置**: `C:\Users\16922\AppData\Local\Programs\Python\Python312\Lib\site-packages`

## 🚀 使用方法

### 1. 快速启动

双击运行 `start_markitdown_mcp.bat` 文件，选择运行模式：

- **模式 1**: STDIO 模式（用于 Claude Desktop）
- **模式 2**: HTTP 模式（用于 Web 接口，地址：http://127.0.0.1:3001）

### 2. 命令行使用

```bash
# STDIO 模式
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m markitdown_mcp

# HTTP 模式
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m markitdown_mcp --http

# 自定义端口
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m markitdown_mcp --http --port 8080
```

### 3. Claude Desktop 配置

#### 步骤 1: 找到配置文件

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

#### 步骤 2: 添加配置

将以下配置添加到文件中（或使用提供的 `claude_desktop_config_example.json`）：

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "C:\\Users\\16922\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
      "args": ["-m", "markitdown_mcp"],
      "env": {}
    }
  }
}
```

#### 步骤 3: 重启应用

重启 Claude Desktop 使配置生效。

## 🔧 主要功能

### 核心功能

- **convert_to_markdown(uri)**: 将各种文档格式转换为 Markdown

### 支持的格式

| 文档类型 | 支持格式           | 说明                       |
| -------- | ------------------ | -------------------------- |
| **文档** | PDF, DOC, DOCX     | 文本提取和格式转换         |
| **表格** | XLS, XLSX, CSV     | 表格数据转换为Markdown表格 |
| **演示** | PPT, PPTX          | 幻灯片内容提取             |
| **图片** | JPG, PNG, GIF, BMP | 图片OCR文字识别            |
| **音频** | MP3, WAV, M4A      | 音频转录（需要额外配置）   |
| **视频** | MP4, AVI, MOV      | 视频内容提取（需要ffmpeg） |
| **网页** | HTML, URL          | 网页内容提取和转换         |

## 💡 使用示例

### 在 Claude Desktop 中使用

```
请帮我将这个 PDF 文件转换为 Markdown：
file:///C:/path/to/document.pdf
```

```
请转换这个在线文档：
https://example.com/document.pdf
```

```
请将这个 Word 文档转换为 Markdown：
file:///D:/documents/report.docx
```

### 常用转换场景

#### 1. 学术论文转换

```
将这篇PDF论文转换为Markdown格式，保持引用和格式：
file:///C:/papers/research_paper.pdf
```

#### 2. 会议记录整理

```
请将这个PowerPoint演示文稿转换为Markdown：
file:///C:/meetings/presentation.pptx
```

#### 3. 数据表格处理

```
将这个Excel表格转换为Markdown表格格式：
file:///C:/data/spreadsheet.xlsx
```

#### 4. 图片文字提取

```
请提取这张图片中的文字并转换为Markdown：
file:///C:/images/screenshot.png
```

## ⚙️ 高级配置

### 环境变量设置

可以通过环境变量自定义行为：

```bash
# 设置临时文件目录
set MARKITDOWN_TEMP_DIR=C:\temp\markitdown

# 设置日志级别
set MARKITDOWN_LOG_LEVEL=DEBUG
```

### 依赖安装

某些功能可能需要额外的依赖：

```bash
# 音频处理（可选）
pip install whisper

# 视频处理（需要 ffmpeg）
# 下载并安装 ffmpeg，添加到系统PATH

# OCR功能增强（可选）
pip install pytesseract
```

## 🔍 故障排除

### 常见问题

#### 1. 文件路径问题

**问题**: 无法找到文件
**解决方案**:

- 确保使用正确的文件路径格式
- 本地文件使用 `file://` 协议
- 路径中的反斜杠需要转义或使用正斜杠

#### 2. 权限问题

**问题**: 无法访问文件
**解决方案**:

- 检查文件权限
- 确保文件未被其他程序占用
- 以管理员身份运行

#### 3. 格式不支持

**问题**: 某些文件格式无法转换
**解决方案**:

- 检查文件是否损坏
- 尝试使用其他格式
- 安装相关依赖

#### 4. 转换质量问题

**问题**: 转换结果不理想
**解决方案**:

- 检查原文件质量
- 对于图片，确保清晰度足够
- 对于PDF，确保是文本型而非扫描型

### 调试方法

#### 启用详细日志

```bash
# 设置环境变量启用调试模式
set MARKITDOWN_LOG_LEVEL=DEBUG
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m markitdown_mcp
```

#### 检查系统状态

```bash
# 检查Python环境
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe --version

# 检查包安装
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m pip list | findstr markitdown
```

## 🔄 更新和维护

### 更新到最新版本

```bash
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m pip install --upgrade markitdown-mcp
```

### 卸载

```bash
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m pip uninstall markitdown-mcp
```

### 重新安装

```bash
# 完全重新安装
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m pip uninstall markitdown-mcp
C:\Users\16922\AppData\Local\Programs\Python\Python312\python.exe -m pip install markitdown-mcp
```

## 📊 性能优化

### 大文件处理

- **分块处理**: 大文件会自动分块处理
- **内存管理**: 系统会自动管理内存使用
- **缓存机制**: 重复文件会使用缓存结果

### 批量转换

虽然工具主要设计为单文件转换，但可以通过脚本实现批量处理：

```python
import os
import subprocess

def batch_convert(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(('.pdf', '.docx', '.pptx')):
            file_path = os.path.join(folder_path, file)
            # 调用转换命令
            print(f"Converting {file}...")
```

## 🔗 相关资源

- [MarkItDown GitHub](https://github.com/microsoft/markitdown)
- [MCP 协议文档](https://modelcontextprotocol.io/)
- [Claude Desktop 官网](https://claude.ai/desktop)

::: tip 💡 使用技巧

1. **文件路径**: 使用绝对路径避免路径问题
2. **格式选择**: PDF文档转换效果通常最好
3. **预处理**: 对于扫描文档，先进行OCR处理
4. **批量处理**: 可以结合脚本实现批量转换
   :::

::: warning ⚠️ 注意事项

- 确保有足够的磁盘空间用于临时文件
- 大文件转换可能需要较长时间
- 某些受保护的文档可能无法转换
- 转换质量取决于原文档的质量
  :::

---

_最后更新: 2024年12月_
