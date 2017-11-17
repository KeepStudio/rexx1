# coding:utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

import re
import encodings

url = 'https://www.crowdfunder.com'

html = requests.get(url).text

# print html


data = {
    'q':'filter',
    'page':'1'
}

data2 = {
    'q':'filter',
    'page':'2'
}
html_post = requests.post(url,data=data).text

# print html_post
print 'html_post获取完成...'
title = re.findall('data-original="h(.*?)" src="',html_post,re.S)
print '网页源码正则判断完成，正在解析下载图片...'
i = 0
for each in title:
    each1 = 'h'+each
    print '正在下载第'+str(i+1)+'张图片...'
    eacha = requests.get(each1)
    fp = open('pic\\' +str(i*100) + '.jpg', 'wb')
    fp.write(eacha.content)
    fp.close()
    print '第' + str(i + 1) + '张图片下载完成！'
    i += 1
