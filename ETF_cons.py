# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:02:20 2020

@author: hs101
"""

import pandas as pd

df1 = pd.read_csv("./ETF_cons/" + "0_ETF_cons510050" + ".csv")
df2 = pd.read_csv("./ETF_cons/" + "0_ETF_cons510180" + ".csv")
# 获得基本数据

#writer = pd.ExcelWriter('自定义.xlsx')
#df1.to_excel(writer, sheet_name='自定义sheet_name0')
#df2.to_excel(writer, sheet_name='自定义sheet_name1')
#writer.save()

with pd.ExcelWriter("./ETF_cons/" + 'a.xls', mode = "w+", decoding='utf-8') as writer:
    df1.to_excel(writer, 'sheet1')
    df2.to_excel(writer, 'sheet2')