#!/usr/bin/env python
# encoding=utf-8
# -*- coding: UTF-8 -*-
import os


def buildAPk():
    print("build apk")
    # os.system("E:")
    os.system(r'E:\\MySpace\\koudailicai\\koudaiStudio')
    # os.system('gradlew assemblerelease')
    # os.chdir(r'E:\\MySpace\\koudailicai\\koudaiStudio')
    os.system('gradlew assemblerelease')