# -*- coding: UTF-8 -*-
import base64
import cookielib
import json
import urllib
import urllib2
from datetime import datetime, timedelta
from time import sleep

# 请求域名
# localHostUrl = 'http://121.199.1.198/koudai_deposit/frontend/web'

localHostUrl = 'https://deposit.koudailc.com'

# 账号
userName = '15039062363'
# 密码
userPasd = '123456'

paypassd = '080524'  # 投资交易密码


def login():
    print ('=====   logining......')

    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    requrl = localHostUrl + "/user/login"
    test_data = {'username': userName, 'password': userPasd}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def getOrder():
    print ('=====  getOrder ......')
    requrl = localHostUrl + "/koudaibao/invest-order"
    test_data = {'money': investMoney, 'voucher_id': '0'}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    jsonRes = json.loads(res);
    global orderId
    orderId = jsonRes['order_id']
    print 'orderId:  ===  ', orderId
    return orderId


def getMoney():
    print ('=====  getRemainMoney ......')
    requrl = localHostUrl + "/deposit/account/remain"
    test_data = {}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    jsonRes = json.loads(res);
    jsonObj = jsonRes['data']
    global investMoney
    investMoney = str(jsonObj['usable_money'] / 100.00)
    # investMoney = str(3969.18)
    print 'invest  money:  ===  ', investMoney


def invest():
    print "do invest()...", datetime.now()
    print ('===  invest ......')

    requrl = localHostUrl + "/koudaibao/invest"
    signStr = 'money=' + investMoney + '&order_id=' + orderId + '&pay_password=' + paypassd + '&use_remain=1**kdlc**'

    print'===sign  ', signStr

    signStr = base64.b64encode(signStr.replace("\n", "").strip())
    signStr = signStr.replace("\n", "")
    print signStr

    test_data_urlencode = '&money=' + investMoney + '&order_id=' + orderId + '&pay_password=' + paypassd + '&use_remain=1&sign=' + signStr
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


SECONDS_PER_DAY = 24 * 60 * 60


def doFirst():
    curTime = datetime.now()
    desTime = curTime.replace(hour=12, minute=00, second=00, microsecond=0)
    print 'desTime:  ', desTime
    delta = desTime - curTime
    sleeptime = delta.total_seconds()
    getOrder()
    print "Now day must sleep %d seconds" % sleeptime
    sleep(sleeptime)
    invest()
    print ' current time:', datetime.now()


investMoney = '0'  # 投资金额
orderId = ''

if __name__ == "__main__":
    login()
    getMoney()
    doFirst()
    # doFunc()
