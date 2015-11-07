#!/usr/bin/env python
# coding: utf-8
### exercise20151031_1.py

"""
爬虫，抓取百度贴吧图片。存储到文件
使用request库抓取一个页面。把其中的图片URL用正则表达式分析出来
*** 此实例对百度贴吧基本适用 ***
"""

import requests
import re
import os

#URL = "http://tieba.baidu.com/p/2460150866"

class paChong(object):
    """docstring for paChong"""
    def __init__(self):
        '''在当前文件夹下新建images文件夹存放抓取的图片'''
        super(paChong, self).__init__()
        self.homeURL = "http://tieba.baidu.com/p/2460150866"    #待抓取URL
        self.images = []
        if not os.path.exists('./images'):  #指定存放目录
            os.mkdir('./images')

    def __load_homePage(self):
        '''加载主页面'''
        homePage = requests.get(self.homeURL).content   #获取主页面所有数据
        return homePage

    def __worker_data(self, htmlPage):
        '''提取HTML文件中图片URL'''
        method = re.compile('^src="(.[^;]+\.jpg)"$')    #编译正则处理规则
        page = re.split(r'\s+', htmlPage)   #将主页面数据拆分为列表
        imageLink = []
        for n in page:          #迭代主页面数据
            if 'jpg' in n  and 'src' in n:
                links = method.findall(n)   #正则匹配
                if links:
                    imageLink = imageLink + links   #合乎条件
        imageLink = tuple(set(imageLink))
        imageDict = {}
        for i in imageLink:     #添加序列ID
            cnt = imageLink.index(i) + 1
            imageDict[cnt] = i
        self.images = imageDict
        return self.images

    def __save_image(self, imageName, content):
        '''保存图片'''
        with open('./images/'+imageName, 'wb') as fp:   #写入指定目录
            fp.write(content)

    def down_images(self):
        '''下载图片'''
        self.__worker_data(self.__load_homePage())
        print "{0} image will be download".format(len(self.images))
        for key,imgURL in self.images.iteritems():
            fileName = imgURL.split('/')[-1]
            print 'download {0} ...'.format(key)
            req = requests.get(imgURL, stream=True)
            self.__save_image(fileName, req.content)


if __name__ == '__main__':
    paChong = paChong()
    paChong.down_images()




