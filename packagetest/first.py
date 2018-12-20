#!/usr/bin/env python
# encoding=utf-8
# -*- coding: UTF-8 -*-
import time

a = "2017-07-04 16:30:00"
print a
# 将其转换为时间数组
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
print '=====timearray:', timeArray
# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print '=====timeStamp: ', timeStamp

thistime = int(time.time())
print '====this.time', thistime

