# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:38:11 2020

@author: hs101
"""

def ifCosnChange(df_groups):
    judge_list = [] 
    length = len(df_groups.columns)
#    print(length)
    for i in range(length-1):
        judge = df_groups.iloc[:,i] == df_groups.iloc[:,i+1]
        if "False" not in judge:
            judge_list.append("True")
            print("No %d: ... True"%(i+1))
    return judge_list
