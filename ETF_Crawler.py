# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:13:34 2020

@author: hs101
"""

import requests
from bs4 import BeautifulSoup
import time,os
import urllib.request,re
#import IPython


try:
    url = "http://www.sse.com.cn/disclosure/fund/etflist/"
    response = requests.get(url)
    html = response.text.encode('iso-8859-1').decode('utf-8')
#    print(html)
#    IPython.embed()
except Exception as err:
    print(err)

soup = BeautifulSoup(html,'lxml')
contents = soup.find_all("div",class_ = "table-responsive sse_table_T01 tdclickable")
contents
pattern = re.compile('')
