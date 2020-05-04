# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:09:46 2020

@author: hs101
"""
#from ETF_Crawler import *
#from ETF_Data import *
from ETF_Crawler import *
from ETF_Data import *


#if __name__=="__main__":
#    info_list = []
#    for i in range(1,11):
#        etf_crawler = ETF_Crawler(i)
#        etf_data = ETF_Data(etf_crawler.dataRaw)
#        etf_data_df1, etf_data_df2 = etf_data.process_dataRaw()
#        info_list.append([etf_data_df1, etf_data_df2])

i = 1
etf_crawler = ETF_Crawler(i)
temp = etf_crawler.get_dataRaw()
etf_data = ETF_Data(etf_crawler.dataRaw)
