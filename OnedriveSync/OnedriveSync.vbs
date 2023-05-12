' 创建和删除OneDriveSync+时间戳的空文件的vbs脚本
' 文件名: OnedriveSync.vbs

' 定义文件名前缀和目录路径
Const PREFIX = "OnedriveSync"
Const DIR_PATH = "C:\Users\username\OneDrive - 北京大学\Sync\"

' 获取当前时间并格式化为时间戳字符串
Dim timestamp
timestamp = Year(Now) & Right("0" & Month(Now), 2) & Right("0" & Day(Now), 2) & _
            Right("0" & Hour(Now), 2) & Right("0" & Minute(Now), 2) & Right("0" & Second(Now), 2)

' 生成文件名
Dim file_name
file_name = PREFIX & timestamp

' 删除之前的同名文件
Dim old_file_path
old_file_path = DIR_PATH & PREFIX & "*"
Set fso = CreateObject("Scripting.FileSystemObject")
For Each file in fso.GetFolder(DIR_PATH).Files
    Set re = New RegExp
    re.Pattern = PREFIX & "\d{14}"
    If re.Test(file.Name) Then
        fso.DeleteFile(file.Path)
    End If
Next

' 创建新的空文件
Dim new_file_path
new_file_path = DIR_PATH & file_name
Set objFile = fso.CreateTextFile(new_file_path)
objFile.Close