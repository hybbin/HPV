import requests
from lxml import etree
import json
import time
from requests import Response

url = "http://wx6.jzapp.fkw.com/23467846/0/mstl_h.jsp?cmd=setWafCk_batchSetDeliveryService"
head = {'Host': 'wx6.jzapp.fkw.com',
        'Connection': 'keep-alive',
        'Content-Length': '124',
        'charset': 'utf-8',
        'cookie': ';'
                  '_siteStatVisitTime=1653547853981;'
                  '_siteStatVisit=visit_23467846;'
                  '_filterVisitTime=fehihllpjlmp;'
                  '_orderSettleDay_113254=20220526;'
                  '_orderBuyer=1;'
                  '_orderSign=234678460113254;'
                  '_pdDay_239_0=20220526;'
                  '_pdDay_217_0=20220526;'
                  'loginMemberAcct=xcx_QSKLCUjyYDaFvi;'
                  '_FSESSIONID=G10QfmlzchSbHRx_;'
                  '_cliid=nR-eJwd3CcFdwrDX;'
                  '_siteStatId=234678460113254;'
                  'loginMemberCacct=ip21719686;'
                  '0pcck300=true;'
                  'is_beta_site_23467846_0=false;'
                  '_siteStatDay=20220526;'
                  '_pdDay_162_0=20220526;'
                  '_siteStatRedirectUv=redirectUv_23467846;'
                  '_siteStatVisitorType=visitorType_23467846;'
                  '113254pcck300=true;'
                  '_siteStatReVisit=reVisit_23467846;'
                  '_pdDay_223_0=20220526;'
                  'loginCaid=23467846;'
                  'siteId=0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3225 MMWEBSDK/20220105 Mobile Safari/537.36 MMWEBID/1687 MicroMessenger/8.0.19.2080(0x28001337) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wx4005c81fa92cf8d9/7/page-frame.html'}
data = {'preOrderId': '579215',
        'batchDeliveryList': '[{"preOrderId":579215,"mctId":0,"selfRaisingMemberInfo":{"prop0":"赵霖",'
                             '"prop1":"13119114565","prop2":"500239199701165752"},"shipType":"","shipSort":8,'
                             '"deliveryStyle":2,"selfRaisingPoint":{"id":1,"name":"重庆五洲妇儿医院","rai":{"prc":"500000",'
                             '"cic":"500100","coc":"500107","sta":"谢家湾正街3号"},"ais":"重庆重庆市九龙坡区谢家湾正街3号",'
                             '"phone":"02360332266","pp":{"lng":106.51412485065521,"lat":29.527649550124753,"pt":1},'
                             '"mai":1,"idm":false},"errorMessage":""}]'}
res = requests.post(url, headers=head, data=data)
response = res.json()
print(response)
# html_text = bytes(bytearray(res.text, encoding='utf-8'))
# html = etree.HTML(html_text)
# print(html)
# contents = html.xpath('//div/xxxx')
