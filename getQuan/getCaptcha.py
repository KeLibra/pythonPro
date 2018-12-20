#! /usr/bin/env python
# coding=utf-8
import cookielib
import urllib
import urllib2
from datetime import datetime, timedelta
from time import sleep


def login():
    print '====  logining......', datetime.now()

    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    requrl = "https://deposit.koudailc.com/user/login"
    test_data = {'username': '15039062363', 'password': '123456'}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def getQuan():
    print ('=========================================================   get quan ......')
    requrl2 = "http://deposit.koudailc.com/user/captcha?refresh"
    test_data2 = {}
    test_data_urlencode2 = urllib.urlencode(test_data2)
    req2 = urllib2.Request(url=requrl2, data=test_data_urlencode2)
    # print req2
    res_data2 = urllib2.urlopen(req2)
    res2 = res_data2.read()
    print res2

if __name__ == "__main__":
    login()
    getQuan()