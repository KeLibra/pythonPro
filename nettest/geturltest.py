import urllib2

url = "https://deposit.koudailc.com/project/get-project-list-all?channelId=16&"

req = urllib2.Request(url)

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
strs = res.decode("UTF-8","ignore").encode("UTF-8")
print strs
