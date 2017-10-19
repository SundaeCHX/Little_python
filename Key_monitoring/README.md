# Key_monitoring

键位监控“病毒”，可打包为 Windows 可执行程序，为了伪装使用 Extension 图标及命名。

记录主机的键位及按键时所在窗口，开机自启动，判断可连接互联网时将记录的日志发送至指定的邮箱。

注意修改 Key_monitoring/Extension.py 代码中的邮箱设置。

修改完成后可利用 PyInstaller 将代码打包为 Extension.exe 可执行程序，打包方法请参考：http://www.pyinstaller.org/ 。

将 Extension.exe 拷贝至目标主机，双击即可无界面启动，开始记录并设置为开机自启。

# 仅可用于学习交流！请勿用于其他用途！


Key_monitoring "virus", can be packaged as a Windows executable program, using Extension's icon and named in order to disguise.

Record the host key and the window, boot from the start, to determine the Internet can be connected to the log will be sent to the specified mailbox.

Note Modify the mailbox settings in the Key_monitoring / Extension.py code.

After the modification is complete, you can use PyInstaller to package the code into the Extension.exe executable. Please refer to the website at http: //www.pyinstaller.org/.

Copy the Extension.exe to the target host, double-click to start the interface, start the record and set the boot from the start.

# Only for learning exchange! Do not use for other purposes!
