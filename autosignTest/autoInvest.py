# -*- coding: UTF-8 -*-
# 口袋项目自动投资脚本
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

investId = '25250'  # 投资项目id
investMoney = '150000'  # 投资金额
voucher_id = '60409248'  # 券的id

paypassd = '080524'  # 投资交易密码

investCount = 1  # 投资的次数


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


def invest():
    print "do invest()...", datetime.now()

    print ('===  invest ......')
    requrl = localHostUrl + "/project/invest-v2"
    signStr = 'id=' + investId + '&is_kdb_pay=0&money=' + investMoney + '&order_id=' + orderId + '&pay_password=' + paypassd \
              + '&redpacket_money=0.00&voucher_id='+voucher_id+'**kdlc**'

    print'===sign  ', signStr

    signStr = base64.b64encode(signStr.replace("\n", "").strip())
    signStr = signStr.replace("\n", "")
    print signStr

    test_data_urlencode = 'id=' + investId + '&is_kdb_pay=0&money=' + investMoney + '&order_id=' + orderId + '&pay_password=' + paypassd \
                          + '&redpacket_money=0.00&voucher_id='+voucher_id+'&sign=' + signStr
    req = urllib2.Request(url=requrl, data=test_data_urlencode)
    # print req2
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def sleepInvest():
    count = 0
    sleepcount = 0
    while (True):
        if (count < investCount):
            print '====执行invest, 第 %d 次   ' % (count + 1)
            print "===currentTime: ", datetime.now()
            # if(count == 3):
            #     global investMoney
            #     investMoney = str(181000);
            invest()
            count = count + 1;
            sleep(sleepcount)
            # sleepcount = sleepcount + 1
        else:
            return

SECONDS_PER_DAY = 24 * 60 * 60


def doFirst():
    curTime = datetime.now()
    desTime = curTime.replace(hour=11, minute=30, second=2, microsecond=0)
    print 'desTime:  ', desTime
    delta = desTime - curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" % sleeptime
    sleep(sleeptime)
    # invest()
    sleepInvest()



if __name__ == "__main__":
    login()
    getOrder();
    doFirst()
