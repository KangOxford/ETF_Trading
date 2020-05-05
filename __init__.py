# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:09:46 2020

@author: hs101
"""
#from ETF_Crawler import *
#from ETF_Data import *
from ETF_Crawler import *
from ETF_Data import *


if __name__=="__main__":
    info_list_ETF_PR_list = []
    info_list_ETF_constitution = []
    for i in range(20,204):
        etf_crawler = ETF_Crawler(i)
        etf_data = ETF_Data(etf_crawler.dataRaw)
        etf_data_df1, etf_data_df2 = etf_data.ETF_PR_list, etf_data.ETF_constitution
        info_list_ETF_PR_list.append(etf_data.ETF_PR_list)
        info_list_ETF_constitution.append(etf_data.ETF_constitution)

# 第20个解码有问题，明早起来继续做
# 'gb2312' codec can't decode byte 0xbb in position 61: illegal multibyte sequence