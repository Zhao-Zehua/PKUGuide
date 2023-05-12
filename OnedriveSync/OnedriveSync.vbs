' ������ɾ��OneDriveSync+ʱ����Ŀ��ļ���vbs�ű�
' �ļ���: OnedriveSync.vbs

' �����ļ���ǰ׺��Ŀ¼·��
Const PREFIX = "OnedriveSync"
Const DIR_PATH = "C:\Users\username\OneDrive - ������ѧ\Sync\"

' ��ȡ��ǰʱ�䲢��ʽ��Ϊʱ����ַ���
Dim timestamp
timestamp = Year(Now) & Right("0" & Month(Now), 2) & Right("0" & Day(Now), 2) & _
            Right("0" & Hour(Now), 2) & Right("0" & Minute(Now), 2) & Right("0" & Second(Now), 2)

' �����ļ���
Dim file_name
file_name = PREFIX & timestamp

' ɾ��֮ǰ��ͬ���ļ�
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

' �����µĿ��ļ�
Dim new_file_path
new_file_path = DIR_PATH & file_name
Set objFile = fso.CreateTextFile(new_file_path)
objFile.Close