# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:07:08 2020

@author: hs101
"""

import pandas as pd
import numpy as np

#from ETF import ETF_recognition 

path = ["./", "../"]
df = pd.read_csv(path[0] + "For_test" + ".csv").drop('Unnamed: 0', axis = 1)
grouped = df.consTicker.groupby(df.tradeDate)
etf_dict = {}

count=1
groups = {}
for name, group in grouped:
#    etf_dict[name] = ETF_recognition(name, group)
#    调用ETF_recognition获得股票的价格涨跌等信息
    group.index = np.arange(len(group))
    print("Name: %s"%name)
    print(group)
    print("Count: %d ................"%count)
    count += 1    
    groups[name] = group
#    break
    
#    print(name)
#    print(group)
    
# df = pd.read_csv(path[1] + "For_tests" + ".csv")

# df = pd.read_csv("For_tests" + ".csv")

df_groups = pd.DataFrame(groups)

