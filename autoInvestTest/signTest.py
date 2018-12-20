# import base64
# s = 'id=38633&is_kdb_pay=0&money=50.0&order_id=2017071445177_459682a56bb9ff&pay_password=123456&redpacket_money=0.00&voucher_id=0**kdlc**'
# a = base64.b64encode(s)
# print a
# print base64.b64decode(a)
# aWQ9Mzg2MzMmaXNfa2RiX3BheT0wJm1vbmV5PTUwLjAmb3JkZXJfaWQ9MjAxNzA3MTQ0NTE3N180NTk2ODJhNTZiYjlmZiZwYXlfcGFzc3dvcmQ9MTIzNDU2JnJlZHBhY2tldF9tb25leT0wLjAwJnZvdWNoZXJfaWQ9MCoqa2RsYyoq


# json_array = {'id': '38633', 'is_kdb_pay': '0', 'money': '50', 'order_id': '111222333', 'pay_password':
#         '123456', 'redpacket_money': '0', 'voucher_id': '0'}
# array = json.loads(json_array)
# for i in array:
#     print i

import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print text
