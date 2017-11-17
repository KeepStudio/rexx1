# coding:utf-8
# -*- coding: utf-8 -*-
import requests
import re




class spider(object):
    def __init__(self):
        print u'开始爬取内容。。。'
# getResource用来获取网页源码
    def getResource(self,url):
        html = requests.get(url)
        return html.text
# changepage用来生成不同页数的链接
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):#这是一个for i  in range()的循环
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)#没有经常用不是很明白
            page_group.append(link)#append() 方法用于在列表末尾添加新的对象。
        return page_group
# geteveryclass用来抓取每个课程块的信息
    def geteveryclass(self,source):
        everyclass = re.findall('<ul class="cf" style="display: block;">.*?</ul>',source,re.S)
        return everyclass
# getinfo用来仓每个课程块中提取出我们要的信息
    def getinfo(self,eachclass):
        info = {}

        info['title'] = re.search('class="lessonimg" title="(.*?)" alt="',eachclass,re.S).group(1)
        info['content'] = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1)
        timeamdlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['classtime'] = timeamdlevel[0]
        info['classlevel'] = timeamdlevel[1]
        # info['levelnum'] = re.search(';">(.*?)学习</em>',eachclass,re.S).group(1)
        # print 'levelnum=' + info['levelnum']
        # print info
        return info
# saveinfo用来保存结果到info.txt文件中
    def saveinfo(self,classinfo):
        f = open('info.txt','a')
        for each in classinfo:
            f.writelines(('title:'+each['title']).encode('utf-8')+'\n')
            f.writelines(('content:'+each['content']).encode('utf-8')+'\n')
            f.writelines(('classtime:'+each['classtime']).encode('utf-8')+'\n')
            f.writelines(('classlevel:'+each['classlevel']).encode('utf-8')+'\n')
            # f.writelines('levelnum:'+each['levelnum']+'\n')
        f.close()


if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url,20)
    for link in all_links:
        print u'正在处理页面：' + link
        html = jikespider.getResource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
        jikespider.saveinfo(classinfo)
