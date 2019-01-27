#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""doc"""

import os
import shutil
import cv2

def image_resize(in_file, out_file, max_long=None, max_kb=None):
    """doc"""
    # pylint: disable=no-member
    shutil.copy2(in_file, out_file)
    if max_long is not None:
        src_image = cv2.imread(out_file)
        src_long = src_image.shape[0]
        if src_image.shape[1] > src_image.shape[0]:
            src_long = src_image.shape[1]
        if src_long > max_long:
            long_rate = round(max_long / src_long - 0.005, 2)
            tar_image = cv2.resize(src_image, (0, 0), fx=long_rate, fy=long_rate)
            cv2.imwrite(out_file, tar_image)
    if max_kb is not None:
        src_kb = round(os.path.getsize(out_file) / 1024 + 0.005, 2)
        if src_kb > max_kb:
            down_rate = 0.05
            kb_rate = round(1 - down_rate, 2)
            src_image = cv2.imread(out_file)
            tar_image = cv2.resize(src_image, (0, 0), fx=kb_rate, fy=kb_rate)
            cv2.imwrite(out_file, tar_image)
            out_kb = round(os.path.getsize(out_file) / 1024 + 0.005, 2)
            while out_kb > max_kb:
                kb_rate = round(kb_rate - down_rate, 2)
                tar_image = cv2.resize(src_image, (0, 0), fx=kb_rate, fy=kb_rate)
                cv2.imwrite(out_file, tar_image)
                out_kb = round(os.path.getsize(out_file) / 1024 + 0.005, 2)

def cvt_gray(in_file, out_file):
    """doc"""
    # pylint: disable=no-member
    src_image = cv2.imread(in_file)
    tar_image = cv2.cvtColor(src_image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(out_file, tar_image)
