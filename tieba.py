#-*-encoding:utf-8-*-
import requests
import  re

# agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
# html = requests.get('https://github.com/timeline.json')
html.encoding = 'utf-8'
# print html.text

# head = re.findall('"color: #039;">(.*?)</a>',html.text,re.S)

# for each in head:
    # print each
name = re.findall('style="color:#666666;">(.*?)</span>',html.text,re.S)

for each in name:
    print each