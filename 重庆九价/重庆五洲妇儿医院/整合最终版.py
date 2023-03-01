import json
import threading
from time import sleep

import requests

# 定义商品ID
# 九价162
# productId = 162
productId = 239

# 运行线程数
ThreadCount = 2
# 延时
SLP = 10
# 预约人姓名
Name = "\"姓名\""
# 预约人电话
PhoneNumber = "\"电话号码\""
# 预约人身份证号码
CardNumber = "\"身份证号码\""
# 预约人已实名微信cookie
Cookie = "Cookies "


def res(url, data):
    res0 = requests.post(url=url, headers=head, data=data)
    return res0


def on():
    try:
        data1 = {'pdInfoList': '[]', 'marketingType': '0', 'marketingId': '0', 'marketingDetailId': '0',
                 'fromDetail': 'true',
                 'optionList': '[]', 'amount': '1', 'productId': productId}

        res1 = res(url1, data1)
        a = res1.text
        if 'preOrderId' in a:
            s = json.loads(a)
            preOrderId = s["preOrderId"]
            print("获取pre0rederld成功！pre0rederld：" + str(preOrderId))
            return preOrderId
        elif '超过可购量' in a:
            return 1
        elif '您购买的商品已售罄' in a:
            return 2
        elif '商品抢购太火爆' in a:
            return 3
        else:
            return 0

    except:
        print("获取pre0rederld出错")


def tw():
    try:
        preOrderId = on()
        if preOrderId == 0:
            return 0
        elif preOrderId == 1:
            return 1
        elif preOrderId == 2:
            return 2
        elif preOrderId == 3:
            return 3
        else:
            data2 = {'preOrderId': preOrderId,
                     'batchDeliveryList': '[{"preOrderId":' + str(
                         preOrderId) + ',"mctId":0,"selfRaisingMemberInfo":{"prop0":' + str(Name) + ','
                                                                                                    '"prop1":' + str(
                         PhoneNumber) + ',"prop2":' + str(CardNumber) + '},"shipType":"","shipSort":8,'
                                                                        '"deliveryStyle":2,"selfRaisingPoint":{"id":1,'
                                                                        '"name":"重庆五洲妇儿医院","rai":{"prc":"500000", '
                                                                        '"cic":"500100","coc":"500107",'
                                                                        '"sta":"谢家湾正街3号"}, '
                                                                        '"ais":"重庆重庆市九龙坡区谢家湾正街3号", '
                                                                        '"phone":"02360332266","pp":{'
                                                                        '"lng":106.51412485065521, '
                                                                        '"lat":29.527649550124753,"pt":1}, '
                                                                        '"mai":1,"idm":false},"errorMessage":""}]'}
            data3 = {'preOrderId': preOrderId, 'orderProp': ''}
            res2 = res(url2, data2)
            res3 = res(url3, data3)
            a = res3.text
            s = json.loads(a)
            orderId = s["orderId"]
            print("提交用户信息、获取orderid成功！orderId：" + str(orderId))
            return orderId
    except:
        print("提交用户信息、获取orderid出错")


def th():
    try:
        orderId = tw()
        if orderId == 0:
            print("出现未知错误")
        elif orderId == 1:
            print("恭喜已经抢到了！赶紧去个人中心付款吧！")
        elif orderId == 2:
            print("还没开始抢呢，或者已经结束了！")
        elif orderId == 3:
            print("请求服务器太频繁了！")
        else:
            data4 = {'orderId': orderId, 'status': '5'}
            res4 = res(url4, data4)
    except:
        print("提交最终订单失败！")


def threads_th(threads_num):
    threads = []
    for i in range(threads_num):
        # 创建线程
        td = threading.Thread(target=th, name='th' + str(i + 1))
        threads.append(td)
    for t in threads:
        # 启动线程
        t.start()
        # for i in threads:
        # 子线程守护
        # i.join()
        # print('数据已全部处理成功')


if __name__ == "__main__":
    head = {'Host': 'wx6.jzapp.fkw.com',
            'Connection': 'keep-alive',
            'Content-Length': '124',
            'charset': 'utf-8',
            'cookie': Cookie,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro Build/RKQ1.200826.002; wv) '
                          'AppleWebKit/537.36 ( '
                          'KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3225 MMWEBSDK/20220105 Mobile '
                          'Safari/537.36 MMWEBID/1687 MicroMessenger/8.0.19.2080(0x28001337) Process/appbrand2 '
                          'WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'Referer': 'https://servicewechat.com/wx4005c81fa92cf8d9/7/page-frame.html'}
    url1 = "https://wx6.jzapp.fkw.com/23467846/0/mstl_h.jsp?cmd=setWafCk_addImmePreOrder"
    url2 = "https://wx6.jzapp.fkw.com/23467846/0/mstl_h.jsp?cmd=setWafCk_batchSetDeliveryService"
    url3 = "https://wx6.jzapp.fkw.com/23467846/0/mstl_h.jsp?cmd=setWafCk_settleOrder"
    url4 = "https://wx6.jzapp.fkw.com/23467846/0/wxmallapp_h.jsp?cmd=checkOrderBeforePay "
    while 1:
        threads_th(ThreadCount)
        sleep(SLP)
