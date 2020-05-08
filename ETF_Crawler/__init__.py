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
    for i in range(1, 300):
        # 后面的数字不需要500 300就够了，最大值是270
        etf_crawler = ETF_Crawler(i)
        etf_data = ETF_Data(etf_crawler.dataRaw, etf_crawler.num_code)
        etf_data_df1, etf_data_df2 = etf_data.ETF_PR_list, etf_data.ETF_constitution
        info_list_ETF_PR_list.append(etf_data.ETF_PR_list)
        info_list_ETF_constitution.append(etf_data.ETF_constitution)
    print(ETF_Data.valid_count)
    print(ETF_Data.valid_list)
    
    with open('./dataRaw/'+"ETF_valid_index.txt", "w+") as file:
        file.write(">>>\n")
        file.write(str(ETF_Data.valid_count)+"\n")
        file.write(">>>\n")
        for item in ETF_Data.valid_list:
            file.write(str(item))
            file.write("\n")

# 为了减轻服务器任务，应该增加一个文件读写操作