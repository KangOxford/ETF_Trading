# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:07:08 2020

@author: hs101
"""

import pandas as pd
import numpy as np

from ETF import ETF_recognition 
from ETF import ETF_decern

from WindPy import w

w.start()


# =============================================================================
# path = ["./", "../"] # 文件路径
# df = pd.read_csv(path[0] + "For_test" + ".csv").drop('Unnamed: 0', axis = 1) #读取测文件
# grouped = df.consTicker.groupby(df.tradeDate)
# etf_dict = {}
# 
# count=1
# groups = {}
# for name, group in grouped:
# 
#     group.index = np.arange(len(group))
#     print("Name: %s"%name)
#     print(group)
#     print("Count: %d ................"%count)
#     count += 1    
#     groups[name] = group
# 
# df_groups = pd.DataFrame(groups)
# 
# for name, group in grouped:
#     etf_dict[name] = ETF_recognition(group, name)
# #    调用ETF_recognition获得股票的价格、涨跌等信息
# =============================================================================
    
    
# =============================================================================
tradeDataList = ['2020-04-01', '2020-05-06']  
path = ["./", "../"] # 文件路径
df = pd.read_csv(path[0] + "For_test" + ".csv").drop('Unnamed: 0', axis = 1) #读取测文件
grouped = df.consTicker.groupby(df.tradeDate)
etf_decern_list = []
for name, group in grouped:
    etf_decern = ETF_decern(group, tradeDataList)
    etf_decern_list.append(etf_decern)
    break
# =============================================================================



w.stop()

