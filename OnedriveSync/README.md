# 使用Onedrive同步任意文件夹

作者：ZhaoZh02

首发日期：2023.05.12

最后修改于：2023.09.17

本教程仅适用于Windows系统

## 1 教育邮箱注册(可选)

~~使用教育邮箱可免费获得至少1 TB的Onedrive空间，有效期至毕业离校。~~

1. ~~打开[Microsoft教育](https://www.microsoft.com/zh-cn/education/products/office)网页~~
2. ~~输入北京大学邮箱(xxx@pku.edu.cn、xxx@stu.pku.edu.cn等)，点击**立即开始**进行注册。~~
3. ~~随指引输入正确的信息即可完成注册。~~

**据北京大学计算中心邮件：**

> 2023年5月16日起，北大师生申请Office365新账号，须填写[此问卷星链接](https://www.wjx.cn/vm/Y5XwfHD.aspx#)，由系统管理员定期开通！“自助注册”功能将关闭。新北大Office365账号默认为北大校园卡号邮箱，具有A1权限；北大教师可申请A3权限，优先为北大Canvas教师分配，由教师教学发展中心管理。

其中学院5位编号可参考[未名一点通](https://bbs.pku.edu.cn/123/)，不足位数用0补足。

**据[Microsoft](https://info.microsoft.com/index.php/email/emailWebview?md_id=1711201)：**

> Office 365 A1 Plus计划将于2024年8月1日停用。

这意味着自2024年8月1日起，教育邮箱的网盘容量将受到限制，您可以选择使用其他订阅计划。

## 2 登录Onedrive

打开Onedrive桌面端应用，登录账号。

使用Clash时可能会造成Onedrive登录失败。

可尝试以下2种方法：

1. Clash->General->UWP Loopback->勾选 ``Onedrive``、``你的账户``、``工作或学校账户``。
2. Clash->Settings->System Proxy->Bypass Domain/IPNet->在末尾添加一行 ``- 'login.microsoftonline.com'``

## 3 设置文件夹链接

Onedrive默认只可同步 ``文档``、``图片``、``桌面``3个系统文件夹，若要同步电脑内的任意文件夹，可进行如下操作：

1. 使用管理员权限打开命令提示符(cmd)。
2. 输入命令 ``mklink /D "OneDrive中目标文件夹的地址" "电脑中目标文件夹的地址"``。

如果输入的命令是 ``mklink /D "C:\Users\username\Onedrive - 北京大学\Test" "D:\Test"``，那么执行该命令后，将在 `C:\Users\username\Onedrive - 北京大学`的目录下创建一个名为 ``Test``的链接，链接目标为 `D:\Test`。

注意，在执行命令前，`C:\Users\username\Onedrive - 北京大学`的目录下不能包含名为 ``Test``的文件夹，否则执行命令后将报错。

## 4 设置自动同步

如果选择不同步 ``文档``、``图片``、``桌面``3个系统文件夹，而只是添加了文件夹链接，Onedrive将不会检测文件夹链接内的变化，从而不会进行同步。

为了解决这个问题，可以在Onedrive内每隔固定的时间(如1分钟)维护一个文件，该文件内容为所有目标文件夹内所有文件名及最后修改时间组成的字符串的哈希值，一旦有任何文件的文件名或最后修改时间发生变化，该哈希值将随之变化。

此过程可通过Python实现，设置步骤如下：

1. 在Onedrive中创建一个文件夹，专门用于放置同步程序和相应的文件，如路径为 `C:\Users\username\Onedrive - 北京大学\Sync`。
2. 下载已打包的[可执行文件](https://github.com/ZhaoZh02/PKUGuide/blob/main/OnedriveSync/OnedriveSync.exe)，再下载[配置文件](https://github.com/ZhaoZh02/PKUGuide/blob/main/OnedriveSync/OnedriveSync.ini)，一同置于上述 ``Sync``文件夹中。
3. 修改[配置文件](https://github.com/ZhaoZh02/PKUGuide/blob/main/OnedriveSync/OnedriveSync.ini)，将 ``cache_path``修改为 ``Sync``文件夹的绝对路径，``folder_path``修改为目标文件夹的路径。``cache_path``只能有一个， ``folder_path``可以添加多行。
4. 键入快捷键 ``Win + R``，输入 ``shell:startup``，回车打开。在弹出的文件夹中新建一个指向[可执行文件](https://github.com/ZhaoZh02/PKUGuide/blob/main/OnedriveSync/OnedriveSync.exe)的快捷方式，即可在开机时自动运行。

提供了可执行文件的[源代码](https://github.com/ZhaoZh02/PKUGuide/blob/main/OnedriveSync/OnedriveSync.py)，可自行打包使用。

## 5 跨平台编辑

Onedrive在Windows、Mac、Android、iOS中均有良好的适配应用，包括Onedrive和Microsoft 365。

例如：以Windows系统为主机，在主机中设置文件自动同步；使用iPad中的Microsoft 365进行云端文档编辑，即可实现同步更改；在macOS中，将Onedrive文件夹加入Finder侧边栏，即可实现云端文件的本地管理，并可全平台同步。
