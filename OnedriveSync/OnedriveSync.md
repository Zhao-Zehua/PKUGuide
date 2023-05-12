# 使用Onedrive同步任意文件夹

作者：ZhaoZh02

首发日期：2023.05.12

最后修改于：2023.05.12

本教程仅适用于Windows系统

## 1 教育邮箱注册(可选)

使用教育邮箱可免费获得至少1 TB的Onedrive空间，有效期至毕业离校。

1. 打开[Microsoft教育](https://www.microsoft.com/zh-cn/education/products/office)网页

<div align="center"><img src="image/使用Onedrive同步任意文件夹的方法/1683881175559.png" width="300"></div>

2. 输入北京大学邮箱(xxx@pku.edu.cn、xxx@stu.pku.edu.cn等)，点击**立即开始**进行注册。
3. 随指引输入正确的信息即可完成注册。

## 2 登录Onedrive

打开Onedrive应用，登录账号。

使用Clash时可能会造成Onedrive登录失败。

可尝试以下2种方法：

1. Clash->General->UWP Loopback->勾选Onedrive、你的账户、工作或学校账户。
2. Clash->Settings->System Proxy->Bypass Domain/IPNet->在末尾添加一行 ``- 'login.microsoftonline.com'``

## 3 设置文件夹链接

Onedrive默认只可同步 ``文档``、``图片``、``桌面``3个系统文件夹，若要同步电脑内的任意文件夹，可进行如下操作：

1. 使用管理员权限打开命令提示符(cmd)。
2. 输入命令 ``mklink /D "OneDrive中目标文件夹的地址" "电脑中目标文件夹的地址"``。

如果输入的命令是 ``mklink /D "C:\Users\username\Onedrive - 北京大学\Test" "D:\Test"``，那么执行该命令后，将在 `C:\Users\username\Onedrive - 北京大学`的目录下创建一个名为 ``Test``的链接，链接目标为 `D:\Test`。

注意，在执行命令前，`C:\Users\username\Onedrive - 北京大学`的目录下不能包含名为 ``Test``的文件夹，否则执行命令后将报错。

## 4 设置自动同步

如果选择不同步 ``文档``、``图片``、``桌面``3个系统文件夹，而只是添加了文件夹链接，Onedrive将不会检测文件夹链接内的变化，从而不会进行同步。

为了解决这个问题，可以在Onedrive内每隔固定的时间(如1分钟)创建并删除一个文件，驱动Onedrive检测所有文件夹。

此过程可通过VBS脚本实现，步骤如下：

1. 在Onedrive中创建一个文件夹，专门用于放置同步脚本和相应的文件，如路径为 `C:\Users\username\Onedrive - 北京大学\Sync`。
2. 下载VBS脚本，用记事本打开，修改第6行 ``Const DIR_PATH="C:\Users\username\OneDrive - 北京大学\Sync\"``为1中文件夹的路径。注意，末尾的 ``\``是必要的。
3. Windows徽标键->任务计划程序->创建基本任务。
   1. 名称和描述：自定。
   2. 触发器：计算机启动时。
   3. 操作：启动程序，在下一步中选择上文提到的VBS脚本。
   4. 完成。
4. 找到创建好的任务，右键->属性。
   1. 点击 ``触发器``标签页，选中已经存在的触发器，点击底部的 ``编辑``按钮。
      1. 高级设置->勾选 ``重复任务间隔``：1分钟。
      2. 高级设置->``持续时间``：无限期。
   2. 点击 ``条件``标签页，取消勾选 ``只有在计算机使用交流电源时才启动此任务``。
   3. 点击 ``设置``标签页，取消勾选 ``允许按需完成任务``，勾选 ``如果过了计划开始时间，立即启动任务``和 ``如果任务失败，按以下频率重新启动``。
   4. 点击右下角 ``确定``，完成设置。

注意，由于学校账户的Onedrive文件夹名中包含中文，VBS文件的编码格式需要设置为GBK。

下面给出了设置任务属性时的参考图片。

<div align="center"><img src="image/使用Onedrive同步任意文件夹的方法/1683886653455.png" width="500"></div>

<div align="center"><img src="image/使用Onedrive同步任意文件夹的方法/1683886748627.png" width="500"></div>

<div align="center"><img src="image/使用Onedrive同步任意文件夹的方法/1683886769285.png" width="500"></div>

<div align="center"><img src="image/使用Onedrive同步任意文件夹的方法/1683886785943.png" width="500"></div>
