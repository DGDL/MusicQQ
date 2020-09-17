#/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2,urllib,json,time,random
from lxml import etree
def QQMusic(Url_input):
	pass
	Url=urllib2.Request(url=Url_input)
	Urlopen=urllib2.urlopen(Url).read()
	xmlHTML=etree.HTML(Urlopen)
	#songmid == 001E8VEF4WFnOY.html
	songmid_link=xmlHTML.xpath('//div[@class="data__actions"]//a[@class="mod_btn js_more"]/@data-mid')
	pass
	#获取songmid 和 guid随机数
	songmid=str(songmid_link[0])
	guid=int(random.random()*2147483647)*int(time.time()*1000)%10000000000
	pass
	data='{"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"%s","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"%s","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'%(guid,guid,songmid)
	pass
	module_url="https://u.y.qq.com/cgi-bin/musicu.fcg?data=%s"%data
	module_Req=urllib2.Request(url=module_url)
	module_Open=urllib2.urlopen(module_Req).read()
	module=json.loads(module_Open)
	pass
	#普通vkey
	vkey=module["req_0"]["data"]["midurlinfo"][0]["vkey"]
	#VIP vkey
	if vkey=="":
		pass
		vkey=module["req"]["data"]["vkey"]
	filename=module["req_0"]["data"]["midurlinfo"][0]["filename"]
	pass

	nomoal="M500"+songmid+".mp3"
	hq="M800"+songmid+".mp3"
	flac="F000"+songmid+".flac"

	# 质量
	musicu_nomoal="http://dl.stream.qqmusic.qq.com/%s?guid=%s&vkey=%s&uin=7162&fromtag=1"%(nomoal,guid,vkey)
	musicu_hq="http://dl.stream.qqmusic.qq.com/%s?guid=%s&vkey=%s&uin=7162&fromtag=1"%(hq,guid,vkey)
	musicu_flac="http://dl.stream.qqmusic.qq.com/%s?guid=%s&vkey=%s&uin=7162&fromtag=1"%(flac,guid,vkey)
	print musicu_nomoal
	print musicu_hq
	print musicu_flac


if __name__ == '__main__':
	Url=raw_input("url:")
	QQMusic(Url)
