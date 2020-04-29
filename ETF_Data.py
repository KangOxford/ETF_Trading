# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:19:50 2020

@author: hs101
"""

import pandas as pd
#import numpy as np
#import os

class ETF_Data:
    def __init__(self,code):
        self.etf_code = code
        self.dataRaw = self.get_dataRaw()
        self.ETF_constitution, self.ETF_PR_list = self.process_dataRaw()
    
    def get_dataRaw(self):
        dataRaw = pd.read_csv(self.etf_code+".ETF", sep='\n', encoding = 'gb2312')
        return dataRaw
    
    def process_dataRaw(self):
        data1 = self.dataRaw[13:-1]
        data2 = self.dataRaw[:12]
    
        data1_split_series = data1["[ETFZL]"].str.split("|")
        datalist1 = []
        for i in range(len(data1_split_series)):
            datalist1.append(data1_split_series[i+13])
        df1 = pd.DataFrame(datalist1).drop([5,6],axis=1)
        
        data2_split_series = data2["[ETFZL]"].str.split('=')
        datalist2 = []
        for i in range(len(data2_split_series)):
            datalist2.append(data2_split_series[i])
        df2 = pd.DataFrame(datalist2)
        return df1,df2

etf_code = "5100100429"
etf_data = ETF_Data(etf_code)


    