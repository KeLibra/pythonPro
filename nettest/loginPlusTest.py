import urllib
import urllib2
from time import ctime
import urllib
import urllib2

from pip._vendor import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

Session = requests.Session()
loginFlag = True

username = "18501610815"
password = "123456"


def login():
    print ('=========   logining......')
    payload = {'username': username, 'password': password}
    loginInfo = Session.post(url="https://deposit.koudailc.com/user/login?clientType=pc", params=payload,
                             verify=False)

    res = loginInfo.text
    print res
    loginFlag = True
    if loginInfo.status_code != 200:
        loginFlag = False
        print loginFlag

    print loginFlag


def getQuan():
    print ('=========   get quan ......')
    requrl2 = "http://deposit.koudailc.com/user-order-form/convert"
    test_data2 = {'id': '4', 'prize_number': '1'}
    # test_data_urlencode2 = urllib.urlencode(test_data2)
    # req2 = urllib2.Request(url=requrl2, data=test_data_urlencode2)
    # print req2
    # res_data2 = urllib2.urlopen(req2)
    # res2 = res_data2.read()
    # print res2
    message = Session.post(url=requrl2, params=test_data2, verify=False)
    print message.text


login()
getQuan()
