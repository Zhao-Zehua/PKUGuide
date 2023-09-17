# 基于校园网的远程桌面

作者：ZhaoZh02

首发日期：2023.05.21

最后修改于：2023.09.17

本教程仅适用于Windows系统作为服务端(被访问的主机)的情况

## 0 原理

局域网内的设备可以通过IP地址定位。1个IP地址在1个局域网中至多对应1台设备。

设备使用端口进行信息的输入和输出，也就是信息的"阀门"。1台设备可开放多个端口。

使用 ``IP地址:端口号``就可以与局域网内的设备通讯。远程桌面的网络设置核心就是这2个参数。

北京大学校园网是一个大型局域网，使用**网线、Wi-Fi(如连接PKU、PKU Secure)和VPN**均可接入。该校园网具有在同一物理位置固定分配同一IP的特性，在很长的一段时间内不会发生变化。基于固定的IP地址，在校园网内可以方便地实现远程桌面，并可以使用VPN在校外访问校园内的主机。

~~2023.05.19起，[Todesk、向日葵在校园网内连接失效](https://bbs.pku.edu.cn/v2/post-read.php?bid=668&threadid=18555592)。~~

## 1 基础设置

在校内连得上再说。

### 1.1 服务端

#### 1.1.1 系统要求

Windows系统仅对专业版开放远程桌面访问，服务端(被访问的主机)需升级为专业版系统。

可以在设置->系统->系统信息->Windows规格查看当前系统版本。

如需升级，可在[北大正版软件共享平台](https://software.pku.edu.cn)获取专业版系统资源。请按照网站内的教程进行系统安装和激活，注意进行重要文件的备份。

#### 1.1.2 物理位置

为保证网络的稳定连接和固定的IP地址，建议将服务端放置于宿舍或实验室，使用网线连接。

如IP不固定，可参考5进行DDNS设置。

#### 1.1.3 开启服务

设置->系统->远程桌面->开启远程桌面，即可开启远程桌面服务。

此页面会显示远程桌面使用的 ``端口号``，默认为3389。

为增强安全性，强烈建议更改此端口号，更改方法见2.1。

#### 1.1.4 获取校园网下的IP地址

**方法1：**

1. 打开命令行程序(cmd、powershell等)。
2. 输入命令 ``ipconfig``，回车。
3. 获取IP地址，格式为xxx.xxx.xxx.xxx。

**方法2：**

1. 打开[北京大学网络服务 - 首页](https://its.pku.edu.cn/)。
2. 点击查看IP，在页面上方将显示 ``IP地址``。

注意，如果连接的是自建路由器，方法1可能得到的是路由器分配的IP地址，如192.168.1.100，此地址无法使用，需使用方法2获得的IP地址；此外，还需在路由器内设置端口转发，参考2.4进行设置。

### 1.2 客户端

#### 1.2.1 Windows

1. Windows系统自带远程桌面软件。键入快捷键 ``Win + R``，输入 ``mstsc.exe``，回车即可打开。
2. 输入1.1.4中获取的服务端IP地址和1.1.3中获得的端口号，形如 ``10.129.200.200:3390``、``[fdf4:17da:124c:2:ddad:6237:52f3:b778]:3390``、``officepc.contoso.com:3390``等均可。
3. 左下角显示选项中有更多设置选项，请按需设置。
4. 进入远程桌面，初次登录时需要输入服务端的账户和密码。

#### 1.2.2 macOS

1. 在Mac App Store下载并安装[客户端](https://apps.apple.com/app/microsoft-remote-desktop/id1295203466?mt=12)。
2. 添加远程桌面信息。由于本人没有macOS设备，请参考1.2.3。

#### 1.2.3 iOS

1. 在App Store下载并安装[客户端](https://apps.apple.com/app/microsoft-remote-desktop/id714464092)。
2. 进入软件，点击左上角加号添加电脑：
   1. 电脑名称：``IP地址:端口号``。
   2. 用户账户：服务端的账户和密码。
   3. 友好名称：即备注，按需设置。
   4. 设备和音频重定向：按需设置。
3. iPad可进入设置->显示，调整分辨率为Retina，获得最佳显示效果。

#### 1.2.4 Android

1. 在Google Play下载并安装[客户端](https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx)。
2. 进入软件，点击右上角加号添加电脑：
   1. PC name：``IP地址:端口号``。
   2. User name：服务端的账户和密码。
   3. 其他按需设置。

## 2 进阶设置

### 2.1 修改默认端口

默认3389端口易受攻击，修改默认端口可以部分提高安全性。

**方法1：**

1. 使用管理员权限打开命令行程序(cmd、powershell等)。
2. 将以下命令中的$portvalue修改为 ``你喜欢或不喜欢的值``，如11451：

   1. ```powershell
      Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "PortNumber" -Value $portvalue
      ```

   2. ```powershell
      New-NetFirewallRule -DisplayName 'RDPPORTLatest-TCP-In' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $portvalue
      ```

3. 重启服务端。

**方法2：**

1. 启动注册表编辑器。
2. 进入以下目录：``HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp``。
3. 修改 ``PortNumber``的值为 ``十进制``的 ``你喜欢或不喜欢的值``。
4. 启动高级安全 Windows Defender 防火墙。
5. 点击 ``入站规则``，``新建规则``：
   1. 规则类型：``端口``。
   2. 协议和端口：``TCP``，``特定本地端口``，``你喜欢或不喜欢的同一个值``。
   3. 操作：``允许连接``。
   4. 名称：``你喜欢或不喜欢的名称``。
   5. 点击 ``完成``。
6. 重启服务端。

### 2.2 关闭不使用的账户使用RDP登陆的权限

1. 启动本地安全策略。

2. 进入以下目录：本地策略 -> 用户权限分配 -> 允许通过远程桌面服务登录。

3. 修改允许使用远程桌面的用户。

### 2.3 启动过多尝试账户锁定

1. 启动本地安全策略。

2. 进入以下目录：账户策略 -> 账户锁定策略 -> 账户锁定阈值。

3. 修改账户锁定阈值（也就是多少次失败尝试后锁定）和锁定时间。

### 2.4 提升帧率上限

远程桌面的默认帧率上限为30帧，可修改注册表以修改上限。

**方法1：**

1. 使用管理员权限打开命令行程序(cmd、powershell等)。
2. 运行下面的命令：

   ```powershell
      Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations' -name "DWMFRAMEINTERVAL" -Value 15
   ```

3. 重启服务端。

**方法2：**

1. 启动注册表编辑器。
2. 进入以下目录：``HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations``。
3. 新建 ``DWORD (32位) 值``，命名为 ``DWMFRAMEINTERVAL``。
4. 修改 ``DWMFRAMEINTERVAL``的值为 ``十进制``的 ``15``。
5. 重启服务端。

此时，帧率上限修改为 15 × 4 = 60 帧。

注意，实际连接时的帧率还取决于网络状况等其他因素。

### 2.5 开启GPU加速

使用远程桌面连接时，默认无法调用GPU，可修改组策略以启用GPU。

1. 启动组策略编辑器。
2. 进入以下目录：``计算机配置->管理模板->Windows组件->远程桌面服务->远程桌面会话主机->远程会话环境``。
3. 编辑 ``将硬件图形适配器应用于所有远程桌面服务会话``，选择 ``已启用``，点击 ``确定``保存设置。
4. 重启服务端。

### 2.6 开启路由器端口转发

如果你的服务端通过连接自建路由器上网，例如在宿舍的网线接口处连接了路由器，那么需要在路由器设置端口转发。

以TP-LINK路由器为例。

1. 登录路由器管理界面，地址通常为 ``192.168.1.1``。
2. 进入以下目录：应用管理->IP与MAC绑定：
   1. 将服务端主机添加到绑定设置中。
   2. 记录由路由器分配的服务端主机的IP地址，通常为 ``192.168.1.xxx``。
3. 进入以下目录：应用管理->虚拟服务器：
   1. 假定你要使用 ``IP地址:9999``来访问服务端 ``11451``端口提供的远程桌面服务。
   2. 点击 ``添加``。
   3. 外部端口：``9999``。
   4. 内部端口：``11451``。
   5. IP地址：刚刚记录的形如 ``192.168.1.xxx``的路由器分配的地址。
   6. 点击 ``保存``。

## 3 其他组网方式

除了利用校园网的局域网环境外，还可以自行构建局域网。

[Zerotier](https://www.zerotier.com/)是一款优秀的异地组网软件，提供了多平台支持。

> ZeroTier lets you build modern, secure multi-point virtualized networks of almost any type. From robust peer-to-peer networking to multi-cloud mesh infrastructure, we enable global connectivity with the simplicity of a local network.

如有需要，请参考[网站](https://www.zerotier.com/)说明进行配置。

Zerotier有moon和planet的进阶用法，如有公网IP可以尝试。

## 4 其他远程软件

由于网络安全原因，Todesk和向日葵等远程软件在校园网内连接失效。

用于游戏串流的Parsec和Moonlight也可用于远程桌面。其优点是性能较强、使用流畅、可调整的参数更多，缺点是对Windows系统的界面适配不如原生远程桌面。此外，Moonlight要求服务端具有可串流的NVIDIA显卡。

从使用需求来看，原生远程桌面更适合办公场景。串流更适合游戏场景。

如有需要，请参考[Parsec](https://parsec.app/)或[Moonlight](https://moonlight-stream.org/)的网站说明进行配置。

## 5 使用DDNS

由于校园网内分配的IP相对固定，这部分就留个小坑，希望计算中心不要给我更新这部分的动力🐶

## 6 参考资料

1. [用于远程桌面服务的远程桌面客户端和远程电脑 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/welcome-to-rds)
2. [Securing Remote Desktop (RDP) for System Administrators | Information Security Office](https://security.berkeley.edu/education-awareness/securing-remote-desktop-rdp-system-administrators)

## 7 致谢

1. 感谢北大未名BBS网友[@ehzon](https://bbs.pku.edu.cn/v2/user.php?uid=306395)对[**2.2**和**2.3**的补充](https://bbs.pku.edu.cn/v2/post-read.php?bid=35&threadid=18641200)。
