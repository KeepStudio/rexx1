# coding:utf-8

import re
import urllib2
import urllib
import requests
import sys
import cookielib


agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

# 请求地址和验证码地址
Post_url = 'http://hhb.cbi360.net/tenderbangsoso.aspx'
url = 'http://hhb.cbi360.net/sg/TenderContent.aspx'
Yzm_url = 'http://user.cbi360.net/ValidCode'
# 将cookie绑定到一个哦opener cookie 由cookie自动管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

# 用户名和密码
unsername = '18328588435'
password = '7896321'
# 用openr访问验证码地址，获取cookie
picture = opener.open(Yzm_url).read()
# 保存验证码到本地
local = open('e:/image.jpg','wb')
local.write(picture)
local.close()
# 打开保存的验证码图片 输入
SecretCode = raw_input('输入验证码：')




data = {
    'page':'0'
}
#获取网页源码
html_get = requests.get(Post_url,data=data,headers = agent).text

print html_get