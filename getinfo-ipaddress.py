#!/usr/bin/env python
#coding:utf-8

import os,sys
import json
import urllib2
import re

class taobao():
	def __init__(self,ip):
		self.ip = ip

	def getInfo(self):
		re = urllib2.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip='+ self.ip).read()
		data_json = json.loads(re)
		re_json = json.dumps(data_json, ensure_ascii=False)
		data = json.loads(re_json)
		city = data['data']['city']
		country = data['data']['country']
		isp = data['data']['isp']
		result = country + ' ' + city + ' ' + isp
		return result



if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8') #中文编码

	ip = sys.argv[1]
	regex_ipaddress = re.compile('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
	if regex_ipaddress.match(ip):
		m = taobao(ip)
		print m.getInfo()
		
	else:
		print '非法IPv4的地址，请重新输入'
	
#	f = open('/root/ipdatabase.txt', 'a') #IP地址列表
#	for i in open('/root/python/iplist', 'r').readlines(1000000):
#		ip = i.strip('\n')
#		m = taobao(ip)
#		result = m.getInfo()
#		print result
#		f.write(result)
#		f.write('\n')
#		time.sleep(0.1)
#	f.close()
