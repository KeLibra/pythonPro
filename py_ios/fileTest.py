# -*- coding: UTF-8 -*-
import os
import sys

'''
    扫描文件夹dir中所有文件，返回文件的相对路径列表
'''
import os
path="F:\\codecopy"
for i in os.walk(path):
    print(i)