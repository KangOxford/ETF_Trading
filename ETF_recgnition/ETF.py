#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:00:39 2020

@author: terrystanley
"""

import uqer
from uqer import DataAPI
SDK = "9279251a79dffd5c01c6e5da12bd0b09d622fcff6af65c883712d98d5b6136ff"
client = uqer.Client(token=SDK)

from WindPy import w

class ETF_recognition:
    '''识别每日成分券中的涨跌停、波动率和换手率
    Attributes：
        tradeDate: str, 交易日期
        consTicker: list, 成分券信息
        consPrice: dict <- float, 成分券价格
        consMaxUpOrDown: dict <- int, 涨跌停       
    '''
    
    def __init__(self, tradeDate, consTicker):
        self.tradeDate = tradeDate
        self.consTicker = consTicker 
        
        self.consPrice = {}
        self.consMaxUpOrDown = {}
        
        self.get_consPrice()
        self.get_cons_maxUpOrDown()
        
    def get_sigle_stock_price(self, stock_code):
        '''
        Args:
            stock_code: str，交易代码
        Returns:
            float变量，一支股票当日的昨收
        '''
        stock_infoRaw = DataAPI.MktEqudGet(secID=u"",ticker=stock_code,tradeDate=self.tradeDate,beginDate=u"",endDate=u"",isOpen="",field=u"",pandas="1")
        # T日交易参考价使用的是昨收
        return stock_infoRaw.loc[:,"preClosePrice"]
    
    def get_consPrice(self):
        '''
        Args: 
            stock_code_list: Series，交易代码序列
        Returns:
            dict，所有股票的价格字典
        '''
        for i in range(len(self.consTicker)):
            Ticker = str(self.consTicker.values[i])
            tempPreClosePrice = self.get_sigle_stock_price(Ticker)
            tempPreClosePrice = float(tempPreClosePrice)
            self.consPrice[Ticker] = tempPreClosePrice
            print("NO. %d, Ticker = %s, PreClosePrice = %f"%(i,Ticker, tempPreClosePrice))
    
    def get_cons_maxUpOrDown(self):
        '''利用wind获得列表中每个股票在特定日期的涨跌停情况
        Args:
            self.consTicker: Series, 交易代码序列
            self.tradeDate: str, 交易时间
        Returns:
            self.consMaxUpOrDown: dict, 交易代码对应是否涨跌停
        '''
        w.start()
        exchange = '.SH'
        if(w.isconnected()):
            length = len(self.consTicker)
            for i in range(length):
                Ticker = str(self.consTicker.values[i])
                wind = w.wsd(Ticker + exchange, "maxupordown", self.tradeDate, self.tradeDate, usedf = True)
                maxUpOrDown = wind[1].iat[0,0]
                self.consMaxUpOrDown[Ticker] = maxUpOrDown
                print("NO. %d, Ticker = %s, MaxUpOrDown = %d"%(i,Ticker, int(maxUpOrDown)))
        else:
            print("Wind Starting Error!")
        w.stop()
        
        








