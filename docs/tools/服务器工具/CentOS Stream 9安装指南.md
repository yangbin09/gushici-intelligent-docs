# CentOS Stream 9 图文详细安装指南

> 一份完整的CentOS Stream 9系统安装教程，适用于VMware虚拟机环境部署

## 📝 内容概述

本文档详细介绍了如何在VMware Workstation Pro 17环境下安装CentOS Stream 9操作系统，包含从镜像下载到系统配置的完整流程。适合系统管理员、运维工程师以及Linux初学者参考使用。

## 🎯 核心要点

### 1. 镜像文件选择

**官方下载源**:

- 官方镜像: https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/
- 清华镜像: https://mirrors.tuna.tsinghua.edu.cn/centos-stream/9-stream/BaseOS/x86_64/iso/
- 阿里云镜像: https://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/x86_64/iso/

**镜像类型对比**:

- `boot.iso`: 网络安装版，体积小但需要联网下载组件，安装过程较慢
- `dvd1.iso`: **推荐选择**，完整安装包，适合离线安装，一次性包含所有必要组件

![镜像下载页面](./../../images/centos-installation/4d5ec788e6ab5cd526d742cfac2a1e28.png)

## 🔧 详细安装步骤

### 第一步：创建虚拟机

1. **启动VMware Workstation Pro**，选择"创建新的虚拟机"

![创建虚拟机](./../../images/centos-installation/63d5d9e6e466eea2f38d5934ec8363c4.png)

2. **选择自定义安装**

![自定义安装](./../../images/centos-installation/017496cefed7e92e3dc75b4166e7ebcd.png)

3. **硬件兼容性选择**，点击"下一步"

![硬件兼容性](./../../images/centos-installation/d80e1a244cddc5c208a8434f22a42f2f.png)

4. **选择"稍后安装操作系统"**

![稍后安装](./../../images/centos-installation/afbfb152e4f85bcc1749c91cf7dc610e.png)

5. **选择操作系统类型**：Linux → CentOS 7 64位

![操作系统选择](./../../images/centos-installation/d7d50d4ddc3350ae18f4a16cb9005cfe.png)

6. **设置虚拟机名称和位置**

![虚拟机命名](./../../images/centos-installation/13e2f6c4f5cc2fb2a6075c5ba17e1cff.png)

### 第二步：配置硬件参数

1. **处理器配置**：建议2核心或以上

![处理器配置](./../../images/centos-installation/f904a476169205ce6e066da7c198408f.png)

2. **内存配置**：建议2GB或以上

![内存配置](./../../images/centos-installation/376c5206d5bcc3b4ee85554f13377e71.png)

3. **网络类型选择**：推荐NAT模式

![网络类型](./../../images/centos-installation/4dd34eba059377f9dc31b21de5c7fee1.png)

4. **I/O控制器类型**：选择推荐选项

![I/O控制器](./../../images/centos-installation/5d226836250617ffa7a7ce3bea8370a1.png)

5. **磁盘类型选择**：选择推荐选项

![磁盘类型](./../../images/centos-installation/017496cefed7e92e3dc75b4166e7ebcd.png)

6. **选择磁盘**：创建新虚拟磁盘

![选择磁盘](./../../images/centos-installation/4259518058b8f1e7dd2c58f34f5d043e.png)

7. **磁盘容量设置**：建议20GB或以上

![磁盘容量](./../../images/centos-installation/1c229af36485cca3f283eb4bc1a7e484.png)

8. **指定磁盘文件位置**

![磁盘文件](./../../images/centos-installation/f51373a119007e5aec2e7287bbd0a47b.png)

### 第三步：配置ISO镜像

1. **自定义硬件设置**

![自定义硬件](./../../images/centos-installation/19040ee850db10b1ef272022000de8f3.png)

2. **选择ISO镜像文件**

![ISO选择](./../../images/centos-installation/19d7121dcf920e5034fcb81f71c33b77.png)

3. **完成虚拟机创建**

![创建完成](./../../images/centos-installation/b58047bed733095b4f44ccbb44cef469.png)

![配置完成](./../../images/centos-installation/3b3fd4dbac305eea478e77b700884136.png)

### 第四步：启动安装程序

1. **开启虚拟机**

![开启虚拟机](./../../images/centos-installation/0f29b0cd2e7e0065f535196845041ed4.png)

2. **选择安装选项**，按回车确认

> 💡 **提示**: 从虚拟机释放鼠标使用 `Ctrl + Alt`

![安装选项](./../../images/centos-installation/72505b66abcaf74065e01a919017db85.png)

3. **等待安装程序加载**

![安装加载](./../../images/centos-installation/f4e860c9c7a592d19c39523b78076650.png)

### 第五步：系统配置

1. **语言选择**：建议选择中文简体

![语言选择](./../../images/centos-installation/330e85d91c6a18736138b2cb5aa13c2a.png)

2. **网络和主机名配置**

![网络配置入口](./../../images/centos-installation/6eb49f54a3550c335c12c869e48ab43b.png)

3. **启用网络连接**

![网络启用](./../../images/centos-installation/5ed62e804ed372eee6636299110ed38f.png)

### 第六步：网络配置（重要）

1. **打开虚拟网络编辑器**

![虚拟网络编辑器](./../../images/centos-installation/2285b7e5706099e01e76f1fbeab38bc0.png)

2. **更改设置**

![更改设置](./../../images/centos-installation/f3330564b4cbb651a71a93106676d4b7.png)

3. **配置NAT网络**

![NAT配置](./../../images/centos-installation/753d0a0df8e94cd7f3001efb26812311.png)

![NAT设置](./../../images/centos-installation/c2ea7f4babd514c997d5a796459f70d4.png)

4. **应用并确定配置**

![应用配置](./../../images/centos-installation/f9625094d268e2a40740b2b836bdda24.png)

### 第七步：磁盘分区配置

1. **安装位置设置**

![安装位置](./../../images/centos-installation/7b5ef5df10464f1c2caeca66cd8f98a2.png)

2. **选择自动分区**（推荐新手使用）

![自动分区](./../../images/centos-installation/843388eae21c7ed83f93faccc3b1ed14.png)

3. **完成分区配置**

![分区完成](./../../images/centos-installation/5204725739fc6b08aeb91fdf518e8858.png)

### 第八步：时间和日期设置

1. **修改时区设置**

![时间设置](./../../images/centos-installation/1b47df2a7504445ac88f7269623bfd7c.png)

2. **选择亚洲/上海时区**

![时区选择](./../../images/centos-installation/79be03c0fdab979d441e999673b0743d.png)

### 第九步：用户配置

1. **设置Root密码**

![Root密码设置](./../../images/centos-installation/0ffff4dd59764cdcfa70f0807b424a3f.png)

![Root密码输入](./../../images/centos-installation/3bd7e0230c99dcebb9159bddf0ec850a.png)

### 第十步：软件选择

1. **选择安装类型**：服务器建议选择"最小安装"

![软件选择](./../../images/centos-installation/950782e6a75dbe45b1d146d0d686321c.png)

![最小安装](./../../images/centos-installation/17e49fd18cf9b631e33d416dfeb83abd.png)

> 💡 **建议**: 对于服务器用途，选择最小安装可以减少系统资源占用和安全风险

### 第十一步：开始安装

1. **开始安装系统**

![开始安装](./../../images/centos-installation/3624a6676a9101a0a371de701e03951d.png)

2. **等待安装完成**

![安装进度](./../../images/centos-installation/633071e1b08fd2967355bc8c686f4f19.png)

3. **安装完成，重启系统**

![重启系统](./../../images/centos-installation/22a512cd955fbf7aef3ce6c97d1726c7.png)

### 第十二步：首次登录

1. **系统启动完成**

![登录界面](./../../images/centos-installation/b3ed44ce2b5f396b1f08753344ee0058.png)

2. **使用Root账户登录**

![登录成功](./../../images/centos-installation/image.png)

## 🎯 VMware虚拟机配置要求

**推荐配置**:

- 处理器: 2核心或以上
- 内存: 2GB或以上
- 硬盘: 20GB或以上
- 网络: NAT模式（推荐）

## 💡 应用建议

### 安装前准备

- [ ] 确保VMware Workstation Pro已正确安装
- [ ] 下载完整的dvd1.iso镜像文件
- [ ] 预留足够的磁盘空间（建议50GB以上）
- [ ] 确保主机网络连接正常

### 安装过程注意事项

- [ ] 选择合适的语言和键盘布局
- [ ] 网络配置务必在安装前完成
- [ ] Root密码设置要符合安全要求
- [ ] 软件选择根据实际用途决定
- [ ] 安装完成后及时更新系统

### 后续配置建议

- [ ] 配置SSH服务以便远程管理
- [ ] 设置防火墙规则
- [ ] 安装必要的开发工具和软件包
- [ ] 配置用户权限和sudo访问
- [ ] 设置系统自动更新策略

## 🔧 常见问题解决

### 网络连接问题

如果安装过程中网络无法连接：

1. 检查VMware网络适配器设置
2. 确认虚拟网络编辑器中NAT配置正确
3. 重启网络服务或重新配置网络

### 安装源问题

如果使用boot.iso遇到安装源问题：

1. 建议改用dvd1.iso完整镜像
2. 检查网络连接稳定性
3. 尝试更换镜像源地址

## 📋 相关标签

`CentOS` `Linux` `系统安装` `VMware` `服务器部署` `虚拟化`

## 🔗 相关链接

- [CentOS官方文档](https://docs.centos.org/)
- [VMware Workstation Pro文档](https://docs.vmware.com/cn/VMware-Workstation-Pro/)

---

_最后更新: 2025-01-27_
_分类: 服务器工具_
_原文来源: CSDN博客_
