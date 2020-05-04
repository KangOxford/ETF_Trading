# 导入必要的包
import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置tushare的pro账户
# 因为只有pro账户才能使用期货的数据
ts.set_token('c00db9d3b3c006758225ef78baa6c08623bf77abb721166227f5ce98')
pro = ts.pro_api()
pro = ts.pro_api('c00db9d3b3c006758225ef78baa6c08623bf77abb721166227f5ce98')


class Index:
    def __init__(self,String_commodity, String_exchange, String_exchange_short_name):
        self.string_commodity = String_commodity
        self.string_exchange = String_exchange
        self.string_exchange_short_name = String_exchange_short_name

        self.index = None
        # 该指标即为单商品指数
        self.index_raw = None
        # 该指标用于计算多商品指数
        self.get_index()
        # 用于获得上面两个属性的值：index, index_raw
        self.Market_Influence = None
        self.Market_Influence_Percentage = None

    def get_data(self):
        # 从Tushare获得数据
        df = pro.fut_daily(ts_code= self.string_commodity+'1901.'+ self.string_exchange_short_name,start_date='20190101',end_date='20191231', exchange=self.string_exchange)
        for i in range(2,13):
            df_temp = pro.fut_daily(ts_code= self.string_commodity+'19'+str(i).zfill(2)+'.'+ self.string_exchange_short_name, start_date='20190101',end_date='20191231',exchange= self.string_exchange)
            df = pd.concat([df, df_temp], ignore_index=True)
        df = df.drop(['pre_close','pre_settle','settle','change1','change2','amount','oi_chg','high','low'],axis = 1)
        return df

    def get_index(self):
        # 输出商品指数，以及其他关键数据
        # 获得[日期：收益率]组合
        # 找出主力合约 <= 对交易量进行排序
        df = self.get_data()
        df['yield'] = (df.close - df.open)* 100/ df.open
        df1 = df.set_index(keys=['trade_date','vol'],append = False, drop = True)
        g1 = df1.reset_index().groupby(['trade_date'])
        g1 = df1.reset_index().groupby(['trade_date'])['vol'].idxmax()
        df2 = df1.iloc[g1]

        # 获得df3，用于生成Index指标
        date_list,vol_list, date_list_modified = [], [], []
        date_raw_data = df2.index
        for i in date_raw_data:
            date_list.append(i[0])
            vol_list.append(i[1])
        for i in date_list:
            date_list_modified.append(pd.Timestamp(i, freq= '1D'))
        df3 = pd.DataFrame({df2.ts_code[0]:list(df2['yield'])}, index = tuple(date_list_modified))

        # 填充缺失值
        # 将没有交易日的，用前后指数的均值来表征；前后没有交易日的，选取最近交易日期
        list_t = list(pd.date_range('20190101','20191231', freq ='1D'))
        df3 = df3.reindex(list_t)
        df3 = df3.interpolate(method= 'akima')
        Index = df3.fillna(df3.mean())
        #返回百分比，单商品指数用收益率来表征

        # 指数的其他数据
        # 该指标不需要填充缺失值
        # 该数据用于计算多商品指数
        Index_raw_data = pd.DataFrame({'Yield':list(df2['yield']),
                            'Open': list(df2['open']),
                            'Close': list(df2['close']),
                            'Vol': vol_list,
                            'Oi': list(df2['oi'])
                            },
                           index = tuple(date_list_modified))
        # return index, index_raw_data
        self.index, self.index_raw = Index, Index_raw_data

# class Index_Vol(Index)；:
#     def __init__(self):
#         self.index_vol = None

#     def get_index_vol(self):


class MultiIndex():
    def __init__(self, Commodity):
        self.commodity = Commodity
        self.multi_index = None
        self.get_multi_index()

    def get_weight(self):
        list_market_influence = []
        for item in self.commodity:
            df = item.index_raw
            df['Price'] = (df.Open + df.Close)/ 2
            a = df.Oi.sum()
            df['Oi_Percentage'] = df.Oi/a
            df['Price_Weighted'] = df.Price * df.Oi_Percentage
            price = df.Price_Weighted.sum()/df.Price_Weighted.count()
            quantity = df.Vol.sum()
            item.Market_Influence = price * quantity
            list_market_influence.append(item.Market_Influence)
        average_market_influence = pd.Series(list_market_influence).mean()
        for item in self.commodity:
            item.Market_Influence_Percentage = item.Market_Influence/ average_market_influence

    def get_multi_index(self):

        self.get_weight()
        # index_series = self.commodity.index.iloc[:,0]
        df = self.commodity[0].index
        list_market_influence = []
        for item in self.commodity:
            df = pd.concat([df, item.index],axis = 1, sort=False)
            list_market_influence.append(item.Market_Influence_Percentage)

        df = pd.concat([df.iloc[:,0],df.drop(df.columns[0],axis=1)],axis=1)
        # df['Index']=df.apply(lambda x: calculate(x,list_market_influence), axis=1)
        df['Index']=df.apply(lambda x:np.dot(np.array(x),np.array(list_market_influence)), axis=1)
        #进行加权平均，需要优化
        Multi_index = pd.DataFrame({'multi_index':df.Index},index= df.index)
        self.multi_index = Multi_index


if __name__ == '__main__':

    # 获得单商品指数
    # 有色金属指数:包含铜、铝、铅、锌、镍、锡。
    # 铜CU、铝AL、锌ZN、铅PB、镍NI、锡SN
    # 这6中期货产品仅在上海期货交易所交易
    index_CU = Index('CU','SHFE','SHF')
    index_AL = Index('AL','SHFE','SHF')
    index_ZN = Index('ZN','SHFE','SHF')
    index_PB = Index('PB','SHFE','SHF')
    index_NI = Index('NI','SHFE','SHF')
    index_SN = Index('SN','SHFE','SHF')
    # index_CU.index
    # index_CU.index_raw

    # 分配权重。合成“有色金属指数”
    index_Commodity = MultiIndex([index_CU,index_AL,index_ZN,index_PB,index_NI,index_SN])
    # index_Commodity.multi_index

    index_Commodity.multi_index.plot(kind ='bar')
    plt.show()

df = pro.index_daily(ts_code='NHNFI.NH',start_date='20190101',end_date='20191231')
