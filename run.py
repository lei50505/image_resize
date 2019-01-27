#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""doc"""

import os
import traceback
import cv

def main():
    """doc"""
    for (dir_path, _, file_names) in os.walk("in"):
        for file_name in file_names:
            in_path = dir_path + os.sep + file_name
            out_path = "out" + os.sep + file_name
            try:
                cv.image_resize(in_path, out_path, 2000, 2000)
                cv.cvt_gray(out_path, out_path)
                print(in_path)
            except BaseException:
                print(in_path + " fail")

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print(traceback.format_exc())
    input("Press Enter to Continue:")
