#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:00:39 2020

@author: terrystanley
"""

import pandas as pd

import uqer
from uqer import DataAPI
SDK = "9279251a79dffd5c01c6e5da12bd0b09d622fcff6af65c883712d98d5b6136ff"
client = uqer.Client(token=SDK)

class ETF_recognition:
    '''识别每日成分券中的涨跌停、波动率和换手率
    Attributes：
        tradeDate: 交易日期
        consTicker: 成分券信息
        consPrice: 成分券价格
    '''
    
    def __init__(self, tradeDate, consTicker):
        self.tradeDate = tradeDate
        self.consTicker = consTicker 
        self.recgnition = []
        self.consPrice = []
        
    def get_sigle_stock_info(stock_code):
        stock_ticker = stock_code
        stock_infoRaw = DataAPI.MktEqudGet(secID=u"",ticker=stock_ticker,tradeDate=u"20200427",beginDate=u"",endDate=u"",isOpen="",field=u"",pandas="1")
        # T日交易参考价使用的是昨收
        stock_info = stock_infoRaw.loc[: ,['secID','ticker','secShortName','tradeDate','preClosePrice']]   
        single_stock_info = stock_info.loc[:,"preClosePrice"]
        return single_stock_info
    
    def get_list_stock_info(stock_code_list):
        # 输入类型是pandas.Series
        list_stock_info = {}
        for i in range(len(stock_code_list)):
            tempPreClosePrice = get_sigle_stock_info(str(stock_code_list[i]))
            list_stock_info[str(stock_code_list[i])] = float(tempPreClosePrice[0])
    
        return list_stock_info
        
        
        
dataRaw = pd.read_csv("data.csv",sep='|',header=None)
data = dataRaw.drop([0,1,7,8],axis=1)
data.columns = pd.Series(["code", 'name', "quantity", "cashAlternatives", "cashPremium"])
stock_code_list = data.code

dict_code_price = get_list_stock_info(stock_code_list)

df_code_price = pd.DataFrame(pd.Series(dict_code_price), columns = ["price"]).reset_index().rename(columns={'index':'code'})

data['price'] = df_code_price['price']
data["amount"] = data.apply(lambda x:x.quantity * x.price, axis = 1)
sum_amount = data.amount.sum()
amount_limit = sum_amount/2
amount_paid = amount_limit*1.1
print(">>>>>>>>>>>>>>>>")
print("对于上证ETF50而言")
print("股票申购开销：%.2f"%amount_limit)
print("现金替代开销：%.2f"%amount_paid)
print("总开销:      %.2f"%(amount_limit+amount_paid))
# 计算最小开销









