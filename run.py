#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import sys
import shutil

WIDTH = 2048

for (dir_path, dir_names, file_names) in os.walk("in"):
    for file_name in file_names:
        file_path = dir_path + os.sep + file_name
        
        print(file_path)
        image = cv2.imread(file_path)
        if image.shape[1] <= WIDTH:
            print("Not Resize")
            shutil.copyfile(file_path, "out" + os.sep + file_name)
            continue
        res = cv2.resize(image, (0, 0), fx=WIDTH/image.shape[1],  fy=WIDTH/image.shape[1])
        cv2.imwrite("out" + os.sep + file_name, res)
        print("Resize")

print("Success")
input("Press Any Key to Exit ...")


