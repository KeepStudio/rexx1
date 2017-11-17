# coding:utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
import encodings

# old_url = 'http://blog.csdn.net/skyeyesxy/article/details/pageNum=2'
# total_page = 20

f = open('re.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('img src="(.*?)">',html,re.S)

i = 0
for each in pic_url:
    print '正在下载：'+ each
    pic = requests.get(each)
    fp = open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    print '第'+str(i+1)+'张图片下载完成'
    i += 1



# title = re.search('<title>(.*?)</title>',html,re.S).group(1)
# print  title

# url = re.findall('src="(.*?)"',html,re.S)
# for each in url:
#     aaa = re.findall('.*?.jpg',each,re.S)
# #     print aaa
# text_fied = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
# text_fied1 = re.findall('<li(.*?)</li>', text_fied, re.S)[0]

# print text_fied1

# text = re.findall('gif">(.*?)</span>', text_fied1, re.S)[0]
# # print  each
# print  text
# for i in range(2, total_page + 1):
#     new_link = re.sub('pageNum=\d','pageNum=%d'%i,old_url,re.S)
#     print new_link
