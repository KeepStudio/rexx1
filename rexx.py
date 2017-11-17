#coding:utf-8
# print 'Hell World'
# for i in range(10):
#     a = i
#     print a

import re

code = 'hadkfalifexxIxxfasdjofja134xxlovexx23345sdfxxyouxx8fse'

# .的使用
# a = 'xy1213'
# b = re.findall('1.',a)
# print b

# *的使用
# a = 'xyxy123'
# b = re.findall('x*',a)
# print b

# a = re.findall('xx.*xx',code)
# print a
# b = re.findall('xx.*?xx',code)
# print b
# c = re.findall('xx(.*?)xx',code)
# print c
# for each in c:
#     print  each

zym = '''4454ewqcczhan43245325gccdsah4324idisahdcc
yiccuugiu9865iccmincce23456wqyeuiowyd'''

s = re.search('cc(.*?)cc',zym,re.S).group(1)
print s
# for each in s:
#     print each
# z = re.findall('(\d+)',zym)
# print  z
