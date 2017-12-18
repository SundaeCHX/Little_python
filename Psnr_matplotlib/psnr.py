#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-18 11:35:43
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home

import os
import numpy as np
import matplotlib.pyplot as plt
import re


def main():
    x = range(0, 300)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    with open('input_256h264_psnr.log', 'r') as f1:
        for line in f1.readlines()[0:300]:
            a1 = line.strip().lstrip().rstrip(',')
            b1 = re.findall('psnr_avg:(.*) psnr_y', a1)
            y1.append(float(b1[0]))
    with open('input_256h265_psnr.log', 'r') as f2:
        for line in f2.readlines()[0:300]:
            a2 = line.strip().lstrip().rstrip(',')
            b2 = re.findall('psnr_avg:(.*) psnr_y', a2)
            y2.append(float(b2[0]))
    with open('input_512h264_psnr.log', 'r') as f3:
        for line in f3.readlines()[0:300]:
            a3 = line.strip().lstrip().rstrip(',')
            b3 = re.findall('psnr_avg:(.*) psnr_y', a3)
            y3.append(float(b3[0]))
    with open('input_512h265_psnr.log', 'r') as f4:
        for line in f4.readlines()[0:300]:
            a4 = line.strip().lstrip().rstrip(',')
            b4 = re.findall('psnr_avg:(.*) psnr_y', a4)
            y4.append(float(b4[0]))
    with open('input_1024h264_psnr.log', 'r') as f5:
        for line in f5.readlines()[0:300]:
            a5 = line.strip().lstrip().rstrip(',')
            b5 = re.findall('psnr_avg:(.*) psnr_y', a5)
            y5.append(float(b5[0]))
    with open('input_1024h265_psnr.log', 'r') as f6:
        for line in f6.readlines()[0:300]:
            a6 = line.strip().lstrip().rstrip(',')
            b6 = re.findall('psnr_avg:(.*) psnr_y', a6)
            y6.append(float(b6[0]))
    plt.figure(figsize=(8, 4))
    plt.plot(x, y1, "r--",
             label="$256Kbps.h264$", linewidth=1)
    plt.plot(x, y2, color="red",
             label="$256Kbps.h265$", linewidth=1)
    plt.plot(x, y3, "b--",
             label="$512Kbps.h264$", linewidth=1)
    plt.plot(x, y4, color="blue",
             label="$512Kbps.h265$", linewidth=1)
    plt.plot(x, y5, "g--",
             label="$1Mbps.h264$", linewidth=1)
    plt.plot(x, y6, color="green",
             label="$1Mbps.h265$", linewidth=1)
    plt.xlabel("picture")
    plt.ylabel("psnr")
    plt.title("PSNR")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
