
# 一张图看懂方案

```
[本地电脑/PicList]
        │  ① 选择图片并上传
        ▼
[阿里云 OSS 存储桶 Bucket]
        │  ② 生成公网访问地址
        │     (可选：自定义域名/CDN)
        ▼
[浏览器/Markdown/博客]
        ③ 引用图片 URL 展示
```


# 0. 你将得到什么

- 一套可直接复用的 **PicList × 阿里云 OSS 图床**配置
    
- 一份**安全合规**的密钥与权限建议（避免泄露与误删）
    
- **上传/复制直链**一键流畅，支持 `x-oss-process` 在线裁剪、缩放与水印
    

---

# 1. 准备工作

- 一个已完成实名认证的 **阿里云账号**
    
- 开通 **对象存储 OSS**（按量计费，图片流量与存储费用低且清晰）
    
- 电脑端安装 **PicList**（GitHub：`Kuingsmile/PicList`，下文会讲怎么配）
https://github.com/Kuingsmile/PicList

![](https://picgoy.oss-cn-shenzhen.aliyuncs.com/Obsidian/img/Pasted%20image%2020250823173447.png)

---

# 2. 创建安全的访问密钥（AccessKey）

> 强烈建议使用 **RAM 子账号** 创建并最小化授权，避免用主账号 AK。

**操作路径（示意）：**
```
阿里云控制台
  → 右上角头像 → AccessKey 管理
  或
  → 资源访问管理 RAM → 用户 → 创建用户 → 访问方式：编程访问
  → 为该用户添加仅限 OSS 的读/写策略
  → 生成 AccessKeyId / AccessKeySecret（只显示一次，一定保存好）
```

**你将拿到：**

- `accessKeyId`
    
- `accessKeySecret`
    

> 文档中已强调：创建密钥后**要注意保存好**，后续在 PicList 中填写使用。


![](https://picgoy.oss-cn-shenzhen.aliyuncs.com/Obsidian/img/Pasted%20image%2020250823171832.png)
# 3. 创建与设置 OSS Bucket

**3.1 新建存储桶**

```
阿里云控制台 → 对象存储 OSS → Bucket 列表 → 创建 Bucket
```

- **Bucket 名称**：全局唯一，建议小写中划线风格，如 `my-blog-images`
    
- **地域（Region）**：就近选择（示例：华东 1 杭州）
    
- **读写权限**：**公共读**（图床通常需要公网可读；否则相册里看不到图）
    

**3.2 记下两个关键要素**

- `bucket`（你的存储桶名）
    
- `area`（**区域代码**，注意不是中文名称！）  
    常见示例：
    
    - 华东 1（杭州） → `oss-cn-hangzhou`
        
    - 华东 2（上海） → `oss-cn-shanghai`
        
    - 华南 1（深圳） → `oss-cn-shenzhen`
        
    - 中国（香港） → `oss-cn-hongkong`
        
    - 日本（东京） → `oss-ap-northeast-1`
        
    - 美国（硅谷） → `oss-us-west-1`
        
    
    > 完整列表见你提供的文件与阿里云官方表格。
    

**3.3（可选）配置 CORS**  
如果未来要在网页里直传或预览，建议按需设置跨域规则（图床多数场景不必强制）。

---

# 4. 规划存储路径与域名

**4.1 存储路径 `path`（可选）**

- 不填：文件会存到 **Bucket 根目录**
    
- 建议：按日期/项目分目录，例：`images/${yyyy}/${MM}/` 或 `blog/` 等
    
- 示例：填 `images/test/` → 文件会进 `images/test/` 目录。
    

**4.2 自定义域名 `customUrl`（可选但推荐）**

- 如果**不填**，直链会使用 **默认外网域名**：
    
    ```
    https://<bucket>.<area>.aliyuncs.com/<path>/<file>
    ```
    
    例：`https://test-bucket.oss-cn-hangzhou.aliyuncs.com/images/test/test.jpg`
    
- 如果**填写**了自定义域名（请加 `http://` 或 `https://`），直链会变为：
    
    ```
    https://你的域名/<path>/<file>
    ```
    
    > 后续可接入 CDN、开通 HTTPS、更换地域不影响链接结构。
    

---

# 5. 安装 & 配置 PicList（最关键）

**5.1 安装**  
前往 `Kuingsmile/PicList` GitHub 项目下载并安装（Windows/macOS/Linux）。

**5.2 在 PicList 中新增“阿里云 OSS 图床”配置**  
在“图床设置”里选择 **Aliyun OSS**，把下列字段填好（示例 JSON 供参考）：

```json
{
  "_configName": "My-OSS-ImageBed",
  "accessKeyId": "你的AccessKeyId",
  "accessKeySecret": "你的AccessKeySecret",
  "bucket": "my-blog-images",
  "area": "oss-cn-hangzhou",
  "path": "images/${yyyy}/${MM}/", 
  "customUrl": "https://img.example.com" 
}
```

- `_configName`：自定义配置名，便于区分
    
- `accessKeyId`/`accessKeySecret`：你在阿里云拿到的密钥（务必保密）
    
- `bucket`：你的存储桶名
    
- `area`：**区域代码**（不是中文名！如 `oss-cn-hangzhou`）
    
- `path`：可选；建议按日期/项目归档
    
- `customUrl`：可选；**务必包含** `http://` 或 `https://` 前缀
    

> 以上字段与注意事项，均来自你提供的文件说明。

**5.3（可选）开启“网站后缀 options”用于在线处理**  
阿里云 OSS 支持图片处理，只需在图片 URL 后追加 `?x-oss-process=...`：

- 等比缩放裁剪：
    
    ```
    ?x-oss-process=image/resize,m_fill,w_100,h_100
    ```
    
- 例：
    
    ```
    https://test-bucket.oss-cn-hangzhou.aliyuncs.com/images/test/test.jpg?x-oss-process=image/resize,m_fill,h_100,w_100
    ```
    
    > 超出免费额度会按量计费；详见 OSS 图片处理文档与费用页。
    

---

# 6. 首次上传与验证

**步骤（配图式说明）**

1. 打开 PicList，选择你刚建好的 **Aliyun OSS** 图床配置
    
2. 拖拽或选择一张本地图片 → 点击上传
    
3. 上传完成后，PicList 会显示 **外链 URL**
    
    - 若设置了 `customUrl` → 形如 `https://img.example.com/xxxx.jpg`
        
    - 未设置 → 形如 `https://<bucket>.<area>.aliyuncs.com/xxxx.jpg`
        
4. 在浏览器打开该 URL：
    
    - 能正常显示图片 → 成功
        
    - 若 403/404 → 见第 8 节“排错”
        

**剪影示意：**

```
[PicList 上传结果面板]
  文件名: banner.jpg
  预览: [√ 能看到缩略图]
  外链: https://img.example.com/2025/08/banner.jpg
  [复制Markdown] [复制URL] [复制HTML]
```

---

# 7. 在博客/文档中引用

- Markdown：`![](https://img.example.com/2025/08/banner.jpg)`
    
- HTML：`<img src="https://img.example.com/2025/08/banner.jpg" alt="banner">`
    
- 需要缩略图/正方形裁剪 → 在 URL 末尾附 `?x-oss-process=...`（见上文）
    

---

# 8. 常见问题与排错清单

|现象|可能原因|解决办法|
|---|---|---|
|打开图片 403|Bucket 非公共读；或策略不允许|把存储桶 **读权限改为“公共读”**；核对 RAM 策略是否含 OSS 读写权限。|
|访问 404|`path` 目录/文件名不对；区分大小写|在 OSS 控制台确认对象真实路径；检查 PicList 的 `path` 填写是否以 `/` 结尾；避免中文或空格。|
|图片能打开但 PicList 相册不预览|桶非公共读或直链域名不通|按上表处理，或在 PicList 配置中临时换成默认外网域名测试。|
|直链很“丑”|未绑定自定义域名|给 Bucket 绑定自定义域名（推荐走 CDN+HTTPS），并把 `customUrl` 改为你的域名（含协议）。|
|处理样式无效|`x-oss-process` 参数写错|对照官方图片处理文档拼写与参数；先用简单的 `resize` 验证。|

---

# 9. 安全与成本优化建议（强烈推荐）

- **最小权限**：用 RAM 子账号，仅授予目标 Bucket 的必要读写权限；必要时加 IP/时间等条件限制。
    
- **密钥管理**：AK 只保存在本机加密存储；丢失/泄露立即在控制台**禁用并更换**。
    
- **路径规划**：用日期/项目分目录，便于生命周期管理与清理。
    
- **CDN 加速**：自定义域名接入 CDN，减少跨地域访问延迟，降低回源成本。
    
- **生命周期规则**：为临时图片设定自动归档/删除策略，控制存储费用。
    
- **水印与缩略**：用 `x-oss-process` 在访问侧处理，省去批量离线处理成本（注意额度与计费）。
    

---

# 10. 附录

## 10.1 常用地域代码对照（节选）

- 华东 1（杭州） `oss-cn-hangzhou`
    
- 华东 2（上海） `oss-cn-shanghai`
    
- 华南 1（深圳） `oss-cn-shenzhen`
    
- 中国（香港） `oss-cn-hongkong`
    
- 日本（东京） `oss-ap-northeast-1`
    
- 美国（硅谷） `oss-us-west-1`
    

> 更多地域与代码在文件中有完整表格可查。**务必填代码，不要填中文名。**

## 10.2 完整配置模板（可复制即用）

```json
{
  "_configName": "My-OSS-ImageBed",
  "accessKeyId": "AKIDEXAMPLE",
  "accessKeySecret": "AKSECRETEXAMPLE",
  "bucket": "my-blog-images",
  "area": "oss-cn-hangzhou",
  "path": "images/${yyyy}/${MM}/${dd}/",
  "customUrl": "https://img.example.com"
}
```

> `path` 支持你手动写入日期目录，保持整洁；`customUrl` 记得加协议头。

## 10.3 常用 `x-oss-process` 示例速查

- 填满 100×100 正方形（可能裁边）：  
    `?x-oss-process=image/resize,m_fill,w_100,h_100`
    
- 宽度 800 等比缩放：  
    `?x-oss-process=image/resize,w_800`
    
- 简单文字水印（示例）：  
    `?x-oss-process=image/watermark,text_5paw5a6J5L2T,size_20,opacity_80`
    

> 详细用法与计费说明请以阿里云官方指南为准。
