# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:13:34 2020

@author: hs101
"""

from urllib import request
import pandas as pd

class ETF_Crawler:
    def __init__(self,num_code):
        self.num_code = num_code
        self.target =  "http://query.sse.com.cn/etfDownload/downloadETF2Bulletin.do?etfType="
        self.url = self.target + str(num_code)
        self.html = self.get_html()
        self.save_to_csv()
        self.dataRaw = self.get_dataRaw()

    def get_html(self):
        try:
            html = request.urlopen(self.url).read()
            html = html.decode('gb2312')
        except:
            html = "Error" + '\n' + "etfType = " + str(self.num_code)
            return html
        else:
            return html

    def save_to_csv(self):
        name = str(self.num_code) + '.ETF'
        with open('./dataRaw/' + name, 'w+', encoding = 'gb2312') as file:
            file.write(self.html)

    def get_dataRaw(self):
        dataRaw = pd.read_csv('./dataRaw/'+str(self.num_code)+".ETF", sep='\n', encoding = 'gb2312')
        return dataRaw

#i = 1
#etf_crawler = ETF_Crawler(i)
#temp = etf_crawler.get_dataRaw()