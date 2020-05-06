class ETF_Raw:
    
    def __init__(self,file_name):
        self.dict_cons = {}
        self.dict_list = {}
        self.file_name = file_name
        self.ETF_list = self.get_ETF_list()
        self.save_all_ETF_data()
        
    # 运行顺序 1
    def get_ETF_list(self):
        with open(self.file_name,'r+') as file:
            lines = file.readlines()
        # 读入ETF_list文件里的信息
        new_lines = []
        for i in range(len(lines)-1):
            new_lines.append(lines[i][:-2] + "0")
        new_lines.append(lines[len(lines)-1][:-1] + '0')
        #for line in lines:
        #    line = line[:-3]+"0"
        #    new_lines.append(line)
        # 去除末尾的1，换成0
        return new_lines 
    # 获得ETF的代号

    # 运行顺序 1
    def save_ETF_data(self, Ticker):
        dir = "./ETF_cons/"
        df1 = DataAPI.FundETFConsGet(secID=u"",ticker=Ticker,beginDate=u"20200429",endDate=u"20200430",field=u"",pandas="1")
        self.dict_list[Ticker] = df1
        # 字典存入申赎表信息：{code: dataframe1}
        df2 = DataAPI.FundETFConsGet(secID=u"",ticker=Ticker,beginDate=u"20200429",endDate=u"20200430",field=u"",pandas="1")
        self.dict_cons[Ticker] = df2
        # 字典存如成分券信息：{code: dataframe2}
    # 取得对应代号ETF的具体信息
    
    def save_all_ETF_data(self):
        for item in self.ETF_list:
            self.save_ETF_data(item)
    # 将所有的ETF_code对应的【申赎表】和【成分券】信息保存到类中

# 运行顺序 2
dir = "./dataRaw/"
# file_name = "ETF_list.txt"
file_name = dir + "ETF_short_list.txt"
# 用于测试，short_list里面只有五个
etf_raw = ETF_Raw(file_name)
# 生成对象，用于获得指定文件中所有etf代码的信息。

# 运行顺序 3
dir = "./ETF_cons/"
with pd.ExcelWriter(dir + 'ETF_list.xls', mode = "w+", decoding='utf-8') as writer:
    for key, value in etf_raw.dict_list.items():   
        value.to_excel(writer, key)
# 执行写入Excel操作 -> 对于ETF_list，即申赎清单

# 运行顺序 3
dir = "./ETF_cons/"
with pd.ExcelWriter(dir + 'ETF_cons.xls', mode = "w+", decoding='utf-8') as writer:
    for key, value in etf_raw.dict_cons.items():   
        value.to_excel(writer, key)
# 执行写入Excel操作 -> 对于ETF_cons，即申赎成分

