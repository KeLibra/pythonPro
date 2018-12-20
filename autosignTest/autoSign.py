# -*- coding: UTF-8 -*-
#  自动签到摇一摇
import base64
import cookielib
import json
import urllib
import urllib2
from datetime import datetime, timedelta
from time import sleep

# 请求域名
# localHostUrl = 'http://121.199.1.198/koudai_deposit/frontend/web'
# localHostUrl = 'https://deposit.koudailc.com'
localHostUrl = 'http://pre-deposit.koudailc.com'

# 账号
# userName = '18501610815'
# userName = '18736005727'
# userName = '13017653080'
# userName = '15039062363'
# 密码
# userPasd = '123456'

# userArray = ["18501610815", "18736005727", "13017653080", "15039062363"]
# psdArray =  ["123456",      "123456",      "123456",      "123456"]


userArray = ["18501610815"]
psdArray =  ["123456"]


def login(uName, uPsd):
    print ('=====   logining......')

    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    requrl = localHostUrl + "/user/login"
    test_data = {'username': uName, 'password': uPsd}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res

def sign():
    print ('=====  auto Sign ......')
    sleep(2)
    signUrl = localHostUrl + '/user-level/go-sign-in'
    test_data = {'type': '2'}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=signUrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def yaoyiyao():
    print ('=====  auto yaoyiyao ......')
    yaoUrl = localHostUrl + '/daily-shake/daily-shake-award'
    test_data = {}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=yaoUrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def doYao():
    count = 0
    while (True):
        sleep(2)
        if (count < 3):
            print '====执行摇一摇, 第 %d 次   ' % (count + 1)
            count = count + 1;
            yaoyiyao()
            # sleepcount = sleepcount + 1
        else:
            return
    sleep(3)



def autoLogin():
    for i in range(len(userArray)):
        print '======自动登录  第 %d 次 ' % (i + 1)
        print '当前账户： ', userArray[i]
        login(userArray[i], psdArray[i])
        sign()
        # doYao()

if __name__ == "__main__":
    autoLogin()






