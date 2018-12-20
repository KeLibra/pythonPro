#! /usr/bin/env python
# coding=utf-8
import cookielib
import urllib
import urllib2
from datetime import datetime, timedelta
from time import sleep





# http://deposit.koudailc.com/user/captcha?refresh  获取验证码的接口

userName = '15039062363'
psd = '123456'


def login():
    print ('=============================================================   logining......')

    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    requrl = "https://deposit.koudailc.com/user/login"
    test_data = {'username': userName, 'password': psd}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def getQuan():
    print ('=========================================================   get quan ......')
    requrl2 = "http://deposit.koudailc.com/user-order-form/convert"
    test_data2 = {'id': '4', 'prize_number': '1', 'imgcode' : 'zake'}
    test_data_urlencode2 = urllib.urlencode(test_data2)
    req2 = urllib2.Request(url=requrl2, data=test_data_urlencode2)
    # print req2
    res_data2 = urllib2.urlopen(req2)
    res2 = res_data2.read()
    print res2


SECONDS_PER_DAY = 24 * 60 * 60


def doFunc():
    print "do Function...", datetime.now()
    getQuan()


def doFirst():
    curTime = datetime.now()
    print 'curTime:  ', curTime
    desTime = curTime.replace(hour=10, minute=0, second=0, microsecond=0)
    print 'desTime:  ', desTime
    delta = desTime - curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" % sleeptime
    sleep(sleeptime)
    doFunc()


if __name__ == "__main__":
    login()
    doFirst()
