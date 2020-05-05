# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:19:50 2020

@author: hs101
"""

import pandas as pd
#import numpy as np
#import os
#class Count_Valid_ETF_Data:
#    def __init

class ETF_Data:
    valid_count = 0
    valid_list = []
    
    def __init__(self,dataRaw,num_code):
        self.dataRaw = dataRaw
        self.num_code = num_code
        self.ETF_constitution, self.ETF_PR_list = self.process_dataRaw()
       

    def process_dataRaw(self):
        if self.dataRaw.columns == "Error":
            df1, df2 = self.dataRaw, self.dataRaw
            return df1, df2
        else:
            ETF_Data.valid_count +=1
            ETF_Data.valid_list.append(self.num_code)
            if list(self.dataRaw.columns)[0][0] == "F":
                data1 = self.dataRaw[18:-1]
                data2 = self.dataRaw[:11]
                df = pd.DataFrame([list(self.dataRaw.columns)[0]], columns = [list(self.dataRaw.columns)[0]])
                data2 = df.append(data2, ignore_index = True)
                print(">>>NO: %d ... Type: 1"%self.num_code)
            else:
                data1 = self.dataRaw[13:-1]
                data2 = self.dataRaw[:12]
                
                print(">>>NO: %d ... Type: 2"%self.num_code)

            data1_split_series = data1.ix[:,0].str.split("|")
            data1_split_series = data1_split_series.reindex(range(len(data1_split_series)),method='bfill')
            # 将索引从18-57 转化为0-39
            datalist1 = []
            for i in range(len(data1_split_series)):
                datalist1.append(data1_split_series[i])
#            print("ok")
            df1 = pd.DataFrame(datalist1).drop([5,6],axis=1)
            #申赎成分券

            data2_split_series = data2.ix[:,0].str.split('=')
            datalist2 = []
            # 申赎基本指标
            for i in range(len(data2_split_series)):
                datalist2.append(data2_split_series[i])
            df2 = pd.DataFrame(datalist2)
            return df1, df2

#etf_code = "5100100429"
#etf_code = "510011"
#etf_data = ETF_Data(etf_code)











