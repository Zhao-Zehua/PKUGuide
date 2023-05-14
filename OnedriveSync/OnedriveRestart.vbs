Option Explicit

Dim objShell, objWMIService, colProcesses, objProcess

' 获取 WMI 服务对象
Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")

' 查询 OneDrive 进程
Set colProcesses = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name='OneDrive.exe'")

' 结束 OneDrive 进程
For Each objProcess In colProcesses
    objProcess.Terminate()
Next

' 创建 Shell 对象
Set objShell = WScript.CreateObject("WScript.Shell")

' 启动 OneDrive
objShell.Run """C:\Program Files\Microsoft OneDrive\OneDrive.exe"""

' 释放对象
Set objShell = Nothing
Set objWMIService = Nothing
Set colProcesses = Nothing
Set objProcess = Nothing

' 退出脚本
WScript.Quit