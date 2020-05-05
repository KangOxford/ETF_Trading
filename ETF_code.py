# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:37:51 2020

@author: hs101
"""


def get_ETF_code(info_list_ETF_PR_list):
    lists = []
    count = 0
    for item in info_list_ETF_PR_list:
        if item.columns == "Error":
            continue
        else:
            a = item.ix[0,1]
            print("NO: %d ... Code: %s"%(count,a))
            count += 1
            lists.append(a)
    return lists

with open ('./dataRaw/ETF_list.txt','w+') as file:
     for item in lists:
         file.write(item+"\n")
         
