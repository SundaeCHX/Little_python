#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-18 11:23:36
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home

from __future__ import division
from __future__ import print_function
import os
import math


def judgeIFOV(d, f, IFOV):
    IFOV1 = int(d) / int(f)
    if (IFOV1 <= float(IFOV)):
        print(u'\n选取的探测器可达到探测/识别要求')
        return True
    else:
        print(u'''
		------------------------------------------
		选取的探测器参数无法达到探测/识别要求
		建议采用以下探测器参数（像元间距/镜头焦距）
		0.417mrad: 17um/41mm  14um/35mm
		0.667mrad: 17um/26mm  14um/21mm
		------------------------------------------
		''')
        return main()


def way1(r, w, d3):
    return int((((int(w)-2*int(r))**2)+int(d3)**2)**0.5+math.pi*int(r))


def way2(r, w, d3, dez):
    a1 = math.atan(math.radians(int(w)/int(d3)))
    a2 = math.acos(math.radians(int(r)*2/int(dez)))
    a3 = (int(dez)**2-4*(int(r)**2))**0.5
    return int(2*int(r)*(math.pi/2-a1-a2)+a3+math.pi*int(r))


def way3(r, w, d3):
    a1 = math.acos(math.radians(int(w)/(2*int(r))))
    a2 = (4*(int(r)**2)-int(w)**2)**0.5
    return int(2*int(r)*a1+math.pi*int(r)+a2-int(d3))


def way4(r, w, d3, n):
    r = r
    d3 = d3
    w1 = int(n)*int(w)
    w2 = (int(n)+1)*int(w)
    l1 = way1(r, w1, d3)
    l2 = way1(r, w2, d3)
    return int((l1+l2)/2)


def calculate(h1, v1, d, f, h, ac, r, IFOV):
    vh = round((int(h1)*int(d))/(int(f)*17.45), 2)
    vv = round((int(v1)*int(d))/(int(f)*17.45), 2)
    ac = float(ac)
    if ac <= vv/2:
        print(u'\n探测器垂直安装角过小，安装角最小为%.2f' % (vv/2))
        return False
    print(u'''
		红外探测器参数
		-------------------------------------
		分辨率             %d x %d
		像元间距           %dum
		镜头焦距           %dmm
		视场角为           %.2f x %.2f
		垂直安装角度       %.2f
		-------------------------------------
		无人机飞行高度为%dm，转弯半径为%dm
		探测/识别所需空间分辨率为 %.3fmrad
		''' % (h1, v1, d, f, vh, vv, ac, h, r, IFOV))
    w = int((2*h*math.tan(math.radians(vh/2)))/math.cos(math.radians(ac-vv/2)))
    print(u'无人机扫描线宽度为%dm' % w)
    d3 = int(h*(math.tan(math.radians(ac-vv/2))+math.tan(math.radians(ac+vv/2))))
    dez = int((w**2+d3**2)**0.5)
    if int(r) <= w/2:
        L = way1(r, w, d3)
        print(u'转弯方式为方式一，单次转弯长度为%dm' % L)
    elif ((w/2 < int(r)) and (int(r) <= dez/2)):
        n = int(2*int(r)/w)+1
        L2 = way2(r, w, d3, dez)
        L4 = way4(r, w, d3, n)
        if L2 <= L4:
            L = L2
            print(u'转弯方式为方式二，单次转弯长度为%dm' % L)
        else:
            L = L4
            print(u'转弯方式为方式四，间隔行数为%d，单次转弯长度为%dm' % (n, L))
    elif int(r) > dez/2:
        n = int(2*int(r)/w)+1
        L3 = way3(r, w, d3)
        L4 = way4(r, w, d3, n)
        if L3 <= L4:
            L = L2
            print(u'转弯方式为方式三，单次转弯长度为%dm' % L)
        else:
            L = L4
            print(u'转弯方式为方式四，间隔行数为%d，单次转弯长度为%dm' % (n, L))
    else:
        return False
    s = 30*20*60	#无人机航程　速度：30m/s 时间：20min
    a = w
    b = 2*w + L
    c = w-s
    x = int((-b+(b**2-4*a*c)**0.5)/(2*a))
    l1 = (x+1)*w
    l2 = int((s-x*L)/(x+1))
    print(u'无人机共转弯%d次，可覆盖区域范围约为%dm x %dm，飞行路径总长度为%dm' % (x, l2, l1, l2*(x+1)+x*L))


def main():
	print(u'请输入无人机飞行高度(m)，转弯半径(m)，探测/识别要求(一般为0.667mrad or 0.417mrad)\neg:200 60 0.667')
	str0 = raw_input()
	parameter0 = str0.split()
	try:
		h = int(parameter0[0])
		r = int(parameter0[1])
		IFOV = float(parameter0[2])
	except Exception as e:
		print(u'输入参数有误，请重新输入！')
		return main()
	else:
		print(u'\n请输入红外探测器参数，分辨率，像元间距(um)，镜头焦距(mm)，垂直安装角度\neg:640 512 17 35 45.00')
		str1 = raw_input()
		parameter1 = str1.split()
		try:
			h1 = int(parameter1[0])
			v1 = int(parameter1[1])
			d = int(parameter1[2])
			f = int(parameter1[3])
			ac = float(parameter1[4])
		except Exception as e:
			print(u'输入参数有误，请重新输入！')
			return main()
	if judgeIFOV(d, f, IFOV):
		calculate(h1, v1, d, f, h, ac, r, IFOV)


if __name__ == '__main__':
    main()
