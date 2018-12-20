# -*- coding: UTF-8 -*-
# 混代码  （代码方法打乱 上马甲包需要）
import os
import random

import re


def chaosCode():
    # 代码地址
    rootdir = "F:\\KDLCNew0411\\KDLCNew0411\\Class\\UserCenter"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if (filename.endswith('.m')):
                with open(os.path.join(parent, filename), 'rt') as f:
                    data = f.read()
                list = re.split(r'@implementation', data)
                if len(list) > 2:
                    print(1)
                    continue
                list = re.split(r'\/\*', data)
                if len(list) > 1:
                    print(2)
                    continue
                list = re.split(r'- \(void\)', data)
                if len(list) < 3:
                    print(3)
                    continue
                header = list[0]
                footer = list[-1]
                list.pop(0)
                list.pop(-1)
                random.shuffle(list)
                with open(os.path.join(parent, filename), 'wt') as f:
                    f.write(header)
                    for lis in list:
                        f.write('- (void)' + lis)
                    f.write('- (void)' + footer)
                    print(os.path.join(parent, filename))


chaosCode()