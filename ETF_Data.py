# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:19:50 2020

@author: hs101
"""

import pandas as pd
#import numpy as np
#import os

class ETF_Data:
    def __init__(self,dataRaw):
        self.dataRaw = dataRaw
        self.ETF_constitution, self.ETF_PR_list = self.process_dataRaw()

    def process_dataRaw(self):
        data1 = self.dataRaw[13:-1]
        data2 = self.dataRaw[:12]
        title = "["+str(self.dataRaw.columns).split("[")[2].split("]")[0]+"]"

        data1_split_series = data1[title].str.split("|")
        datalist1 = []
        for i in range(len(data1_split_series)):
            datalist1.append(data1_split_series[i+13])
        df1 = pd.DataFrame(datalist1).drop([5,6],axis=1)

        data2_split_series = data2[title].str.split('=')
        datalist2 = []
        for i in range(len(data2_split_series)):
            datalist2.append(data2_split_series[i])
        df2 = pd.DataFrame(datalist2)
        return df1,df2

#etf_code = "5100100429"
#etf_code = "510011"
#etf_data = ETF_Data(etf_code)



