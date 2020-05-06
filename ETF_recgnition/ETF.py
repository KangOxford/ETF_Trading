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
        consPrice: dict{str: Series}, 成分券价格
        consMaxUpOrDown: dict{str: int}, 涨跌停       
    '''
    
    def __init__(self, consTicker, tradeDate):
        self.tradeDate = tradeDate
        self.consTicker = consTicker 
        
        self.consPrice = {}
        self.consMaxUpOrDown = {}
        self.consTurn = {}
        self.consSwing = {}
        
        self.get_consPrice(self.tradeDate, self.tradeDate)
        self.get_cons_maxUpOrDown(self.tradeDate, self.tradeDate)
        self.get_cons_turn(self, self.tradeDate, self.tradeDate)
        self.get_cons_swing(self, self.tradeDate, self.tradeDate)
        
    def get_sigle_stock_price(self, stock_code, beginDate, endDate):
        '''
        Args:
            stock_code: str，交易代码
        Returns:
            float变量，一支股票当日的昨收
        '''
        stock_infoRaw = DataAPI.MktEqudGet(secID=u"",ticker=stock_code,tradeDate=u"",beginDate=beginDate,endDate=endDate,isOpen="",field=u"",pandas="1")
        # T日交易参考价使用的是昨收
        return stock_infoRaw.loc[:,"preClosePrice"]
    
    def get_consPrice(self, beginDate, endDate):
        '''
        Args: 
            stock_code_list: Series，交易代码序列
        Returns:
            dict，所有股票的价格字典
        '''
        for i in range(len(self.consTicker)):
            Ticker = str(self.consTicker.values[i])
            tempPreClosePrice = self.get_sigle_stock_price(Ticker, beginDate, endDate)
#            tempPreClosePrice = float(tempPreClosePrice)
            self.consPrice[Ticker] = tempPreClosePrice # self.consPrice: dict{str: Series}
#            print("NO. %d, Ticker = %s"%(i,Ticker))
            print(" %.2d "%i, sep=">", end = '')       
        print("get_consPrice ...... Done!")
        print("\n")
        
    def get_cons_maxUpOrDown(self, beginDate, endDate):
        '''利用wind获得列表中每个股票在特定日期的涨跌停情况
        Args:
            self.consTicker: Series, 交易代码序列
            self.tradeDate: str, 交易时间
        Returns:
            self.consMaxUpOrDown: dict, 交易代码对应是否涨跌停
        '''
#        w.start()
        exchange = '.SH'
        if(w.isconnected()):
            length = len(self.consTicker)
            for i in range(length):
                Ticker = str(self.consTicker.values[i])
                wind = w.wsd(Ticker + exchange, "maxupordown", beginDate, endDate, usedf = True)
                maxUpOrDown = wind[1]
                self.consMaxUpOrDown[Ticker] = maxUpOrDown
#                print("NO. %d, Ticker = %s"%(i,Ticker))
                print(" %.2d "%i, sep=">", end = '')
            print("get_cons_maxUpOrDown ...... Done!")
            print("\n")
        else:
            print("Wind Starting Error!")
#        w.stop()

    def get_cons_turn(self, beginDate, endDate):
        '''利用wind获得列表中每个股票在特定日期的换手率情况
        Args:
            self.consTicker: Series, 交易代码序列
            self.tradeDate: str, 交易时间
        Returns:
            self.consTurn: dict, 交易代码对应是否涨跌停
        '''
#        w.start()
        exchange = '.SH'
        if(w.isconnected()):
            length = len(self.consTicker)
            for i in range(length):
                Ticker = str(self.consTicker.values[i])
                wind = w.wsd(Ticker + exchange, "turn", beginDate, endDate, usedf = True)
                consTurn = wind[1]
                self.consTurn[Ticker] = consTurn
#                print("NO. %d, Ticker = %s"%(i,Ticker))
                print(" %.2d "%i, sep=">", end = '')
            print("get_cons_turn ...... Done!")
            print("\n")
        else:
            print("Wind Starting Error!")
#        w.stop()

    def get_cons_swing(self, beginDate, endDate):
        '''利用wind获得列表中每个股票在特定日期的振幅情况
        Args:
            self.consTicker: Series, 交易代码序列
            self.tradeDate: str, 交易时间
        Returns:
            self.consSwing: dict, 交易代码对应是否涨跌停
        '''
#        w.start()
        exchange = '.SH'
        if(w.isconnected()):
            length = len(self.consTicker)
            for i in range(length):
                Ticker = str(self.consTicker.values[i])
                wind = w.wsd(Ticker + exchange, "turn", beginDate, endDate, usedf = True)
                consSwing = wind[1]
                self.consSwing[Ticker] = consSwing
#                print("NO. %d, Ticker = %s"%(i,Ticker))
                print(" %.2d "%i, sep=">", end = '')
            print("get_cons_swing ...... Done!")
            print("\n")
        else:
            print("Wind Starting Error!")
#        w.stop()


class ETF_decern(ETF_recognition):
    '''
    继承自ETF_recognition
    区别在于ETF_recognition针对的是一天，tradeDate按一天计算
    但是ETF_decern针对的是一段时间。
    在计获得时间序列数据时，ETF_decern在速度上有优势。
    '''
    def __init__(self, consTicker, tradeDateList):
        self.consTicker = consTicker 
        self.tradeDateList = tradeDateList
        
        self.consPrice = {}
        self.consMaxUpOrDown = {}
        self.consTurn = {}
        self.consSwing = {}
        
        self.get_consPrice(self.tradeDateList[0], self.tradeDateList[-1]) #重载初始化函数     
        self.get_cons_maxUpOrDown(self.tradeDateList[0], self.tradeDateList[-1]) #重载初始化函数
        self.get_cons_turn(self.tradeDateList[0], self.tradeDateList[-1]) #重载初始化函数
        self.get_cons_swing(self.tradeDateList[0], self.tradeDateList[-1]) #重载初始化函数
        
        
# 还可以优化，把max turn 和 swing 三个放到一起。







