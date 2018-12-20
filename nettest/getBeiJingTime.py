import httplib
import time
import os


def get_webservertime(host):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("GET", "/")
        r = conn.getresponse()
        ts = r.getheader('date')
        print '============================'
        print ts
        print '============================'
        ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        print '11111111', ltime
        ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
        print '22222222', ttime
        dat = "date %u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
        tm = "time %02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
        currenttime = "%u-%02u-%02u %02u:%02u:%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday, ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
        print '33333333',currenttime
        print (dat, tm)
    except:
        print False


get_webservertime('www.beijing-time.org')