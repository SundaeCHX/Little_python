#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-14 01:30:06
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home

# coding: utf-8
 
import os
import time
import numpy as np 
import cv2
from PIL import Image, ImageDraw, ImageGrab
import socket
import math


def screenshot():
	im = ImageGrab.grab((467, 0, 892, 768))
	im.save('start.png','png')

def main():
	for n in range(0,10000):
		screenshot()
		filename='start.png'
		img_rgb = cv2.imread(filename,0)
		template=cv2.imread('chess.png',0)
		w, h = template.shape[::-1]
		res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
		min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
		cv2.rectangle(img_rgb,max_loc,(max_loc[0]+w,max_loc[1]+h),255,2)
		center_loc=(max_loc[0]+18,max_loc[1]+79)
		special_board = ['music.png','cess.png','mofang.png']
		special=0
		for i in special_board:
			template_cess=cv2.imread(i,0)
			cess_w,cess_h=template_cess.shape[::-1]
			cess_res = cv2.matchTemplate(img_rgb,template_cess,cv2.TM_CCOEFF_NORMED)
			cess_min_val,cess_max_val,cess_min_loc,cess_max_loc = cv2.minMaxLoc(cess_res)
			if cess_max_val > 0.90 and (cess_max_loc[1]+cess_h) < max_loc[1]+h:
				cv2.rectangle(img_rgb,cess_max_loc,(cess_max_loc[0]+cess_w,cess_max_loc[1]+cess_h),255,2)
				print("success")
				if i == 'cess.png':
					x_center,y_center=cess_max_loc[0]+51,cess_max_loc[1]+30
					special=1
				elif i == 'mofang.png':
					x_center,y_center=cess_max_loc[0]+49,cess_max_loc[1]+33
					special=1
				else:
					x_center,y_center=cess_max_loc[0]+59,cess_max_loc[1]+37
					special=1
			else:
				pass
		template_not=cv2.imread('not.png',0)
		not_w, not_h = template_not.shape[::-1]
		not_res = cv2.matchTemplate(img_rgb,template_not,cv2.TM_CCOEFF_NORMED)
		not_min_val,not_max_val,not_min_loc,not_max_loc = cv2.minMaxLoc(not_res)
		
		if not_max_val > 0.95:
			cv2.rectangle(img_rgb,not_max_loc,(not_max_loc[0]+not_w,not_max_loc[1]+not_h),255,2)
			x_center,y_center=not_max_loc[0]+10,not_max_loc[1]+6
			
		else:
			if special==0:
				img=img_rgb.copy()
				img=cv2.GaussianBlur(img,(5,5),0)
				canny=cv2.Canny(img,1,10)
				canny_h,canny_w=canny.shape
				for k in range(max_loc[1]-10,max_loc[1]+100):
					for b in range(max_loc[0]-10,max_loc[0]+50):
						canny[k][b]=0

				y_top=np.nonzero([max(row) for row in canny[130:]])[0][0] + 130
				x_top = int(np.mean(np.nonzero(canny[y_top])))
				
				y_bottom=y_top+15
				for row in range(y_bottom,canny_h):
					if canny[row,x_top] != 0:
						y_bottom=row
						break
				x_center,y_center=x_top,(y_top+y_bottom)//2
				
				'''
				x_center=x_top
				y_center=center_loc[1]-int(abs(x_top - center_loc[0])*math.sqrt(3)/3)
				'''
				cv2.circle(canny,(x_center,y_center),2,255,-1)
				cv2.circle(canny,(x_top,y_top),2,255,-1)
				cv2.line(canny,(x_center,y_center),(center_loc[0],center_loc[1]),255,1)
				filename2='last_canny'+str(n)+'.png'
				cv2.imwrite(filename2,canny)
			else:
				pass
		cv2.circle(img_rgb,(x_center,y_center),2,255,-1)
		cv2.circle(img_rgb,center_loc,2,255,-1)
		distance=(center_loc[0]-x_center)**2+(center_loc[1]-y_center)**2
		distance=distance**0.5
		print(distance)
		cv2.line(img_rgb,(x_center,y_center),(center_loc[0],center_loc[1]),0,1)
		filename1='last_img'+str(n)+'.png'
		cv2.imwrite(filename1,img_rgb)

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('169.254.227.235', 9999))
		if special == 1:
			s.send(str(1000+distance).encode('utf-8'))
		else:
			s.send(str(distance).encode('utf-8'))
		s.close()
		time.sleep(2)
		
	
if __name__ == '__main__':
	main()
