#!/usr/bin/env python

import os,sys
import json
import urllib2

class taobao():
	def __init__(self,ip):
		self.ip = ip

	def getInfo(self):
		re = urllib2.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip='+ self.ip).read()
		data_json = json.loads(re)
		re_json = json.dumps(data_json, ensure_ascii=False)
		#data = json.loads(re_json, encoding='utf-8')
		data = json.loads(re_json)
		isp = data['data']['isp']
		result = self.ip + ':' + isp
		return result
		#print  self.ip,':',data['data']['isp']
		#data_isp = data['data']


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	f = open('/root/ipdatabase.txt', 'a')
	for i in open('/root/python/iplist', 'r').readlines(1000000):
		ip = i.strip('\n')
		m = taobao(ip)
		result = m.getInfo()
		print result
		f.write(result)
		f.write('\n')
		time.sleep(0.1)
	f.close()
