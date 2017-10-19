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


from __future__ import division
import PIL
import Image
import numpy
import os
import random
import numexpr
import time
import ImageFont
import ImageDraw

STAG = time.time()

root = ''
W_num = 16
H_num = 16
W_size = 400
H_size = 400

aval = []


def getAllPhotos():
    root = os.getcwd() + '/'
    src = root + 'photos/'
    for i in os.listdir(src):
        if os.path.splitext(src + i)[-1] == '.jpg' or '.JPG':
            aval.append(src + i)


def transfer(img_path, dst_width, dst_height):
    im = Image.open(img_path)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    s_w, s_h = im.size

    if s_w < s_h:
        im = im.rotate(90)

    resized_img = im.resize((dst_width, dst_height))
    print numpy.array(resized_img)[:dst_height, :dst_width]
    return numpy.array(resized_img)[:dst_height, :dst_width]


def createNewImg():
    iW_size = W_num * W_size
    iH_size = H_num * H_size
    for alpha in [0.35, 0.4, 0.45, 0.5, 0.55]:
        I = numpy.array(transfer(root + 'target.jpg', iW_size, iH_size))
        I = numexpr.evaluate('''I*(1-alpha)''')
        for i in range(W_num):
            for j in range(H_num):
                SH = I[(j * H_size):((j + 1) * H_size),
                       (i * W_size):((i + 1) * W_size)]
                DA = transfer(random.choice(aval), W_size, H_size)
                res = numexpr.evaluate('''SH+DA*alpha''')
                I[(j * H_size):((j + 1) * H_size),
                  (i * W_size):((i + 1) * W_size)] = res
        Image.fromarray(I.astype(numpy.uint8)).save('imgcloud_%s.jpg' % alpha)


def createNewImge():
    iW_size = W_num * W_size
    iH_size = H_num * H_size
    print root
    I = numpy.array(transfer(root + 'target.jpg', iW_size, iH_size)) * 1.0

    for i in range(W_num):
        for j in range(H_num):
            s = random.choice(aval)
            res = I[j * H_size:(j + 1) * H_size, i * W_size:(i + 1) * W_size] * numpy.array(
                transfer(s, W_size, H_size)) / 255
            I[j * H_size:(j + 1) * H_size, i * W_size:(i + 1) * W_size] = res

    img = Image.fromarray(I.astype(numpy.uint8))
    img = img.point(lambda i: i * 1.5)
    img.save('imgcloud.jpg')


if __name__ == '__main__':
    getAllPhotos()
    createNewImg()
    createNewImge()
    print "Total Time %s" % (time.time() - STAG)
