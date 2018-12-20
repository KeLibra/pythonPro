# -*- coding: UTF-8 -*-
#  存管项目自动投资脚本
import base64
import cookielib
import json
import urllib
import urllib2
from datetime import datetime, timedelta
from time import sleep

# 请求域名
localHostUrl = 'http://www.pt.koudailc.com/frontend/web'
# localHostUrl = 'https://deposit.koudailc.com'

# 账号
userName = '13699995555'
# 密码
userPasd = '123456'

investId = '40810'  # 投资项目id
investMoney = '50'  # 投资金额
voucher_id = '0'  # 券的id

paypassd = ''  # 投资交易密码


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
    requrl = localHostUrl + "/project/invest-order"
    test_data = {'money': investMoney, 'voucher_id': '0', 'is_deposit': '1'}
    test_data_urlencode = urllib.urlencode(test_data)
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res
    jsonRes = json.loads(res);
    orderId = jsonRes['order_id']
    print 'orderId:  ===  ', orderId
    return orderId


def invest():
    print "do invest()...", datetime.now()
    orderId = getOrder();

    print ('===  invest ......')
    requrl = localHostUrl + "/deposit/project/invest?clientType=ios"
    signStr = 'id=' + investId + '&money=' + investMoney + '&order_id=' + orderId + '&redpacket_money=0.00&voucher_id=' + voucher_id + '**kdlc**'

    print'===sign  ', signStr

    signStr = base64.b64encode(signStr.replace("\n", "").strip())
    signStr = signStr.replace("\n", "")
    print signStr
    # voucher_id = 0 & money = 50 & order_id = 2017071445177_859683c0f77f08 & is_kdb_pay = 0 & pay_password = 123456 & sign = aWQ9Mzg2MzMmaXNfa2RiX3BheT0wJm1vbmV5PTUwLjAmb3JkZXJfaWQ9MjAxNzA3MTQ0NTE3N184NTk2ODNjMGY3N2YwOCZwYXlfcGFzc3dvcmQ9MTIzNDU2JnJlZHBhY2tldF9tb25leT0wLjAwJnZvdWNoZXJfaWQ9MCoqa2RsYyoq & id = 38633 & redpacket_money = 0
    # test_data_urlencode = urllib.urlencode(test_data)
    test_data_urlencode = 'id=' + investId + '&money=' + investMoney + '&order_id=' + orderId + '&redpacket_money=0.00&voucher_id=' + voucher_id + '&invest_sign=' + signStr
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


SECONDS_PER_DAY = 24 * 60 * 60


def doFirst():
    curTime = datetime.now()
    desTime = curTime.replace(hour=15, minute=00, second=01, microsecond=0)
    print 'desTime:  ', desTime
    delta = desTime - curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" % sleeptime
    # sleep(sleeptime)
    count = 0
    sleepcount = 10
    while (True):
        if (count < 2):
            print '====执行invest, 第 %d 次   ' % (count + 1)
            print "===currentTime: ", datetime.now()
            sleep(sleepcount)
            invest()
            count = count + 1;
            # sleepcount = sleepcount + 1
        else:
            return


if __name__ == "__main__":
    login()
    doFirst()
