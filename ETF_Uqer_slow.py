import pandas as pd
# 导入必要的包

# 运行顺序 1
def get_ETF_list(file_name):
    with open(file_name,'r+') as file:
        lines = file.readlines()
    # 读入ETF_list文件里的信息
    new_lines = []
    #for i in range(len(lines)-1):
    #    new_lines.append(lines[i][:-2] + "0")
    #new_lines.append(lines[len(lines)-1][:-1] + '0')
    for line in lines:
        line = line[:-2]+"0"
        new_lines.append(line)
    #去除末尾的1，换成0
    return new_lines 
# 获得ETF的代号

# 运行顺序 1
def write_ETF_Data(Ticker):
    dir = "./ETF_cons/"
    df1 = DataAPI.FundETFConsGet(secID=u"",ticker=Ticker,beginDate=u"20190101",endDate=u"20200430",field=u"",pandas="1")
    file1 = dir + "list" + "_" + Ticker + "_" + ".csv"
    df1.to_csv(file1, mode = "w+")
    print(file1)
    df2 = DataAPI.FundETFConsGet(secID=u"",ticker=Ticker,beginDate=u"20190101",endDate=u"20200430",field=u"",pandas="1")
    file2 = dir + "cons" + "_" + Ticker + "_" + ".csv"
    df2.to_csv(file2, mode = "w+")
    print(file2)
    print('.....')
    # 把dataframe文件变成csv文件
# 取得对应代号ETF的具体信息

# 运行顺序 2
dir = "./dataRaw/"
file_name = dir + "ETF_list.txt"
#file_name = dir + "ETF_short_list.txt"
#file_name = dir + "ETF_single.txt"
# 用于测试，short_list里面只有五个
ETF_list = get_ETF_list(file_name)
# 获得所有的ETF代码

for item in ETF_list:
    write_ETF_Data(item)
# 把dataframe文件变成csv文件


# 运行顺序 3
print(".........")
dir = "./ETF_cons/"
with pd.ExcelWriter(dir + 'ETF_list.xls', mode = "w+", decoding='utf-8') as writer:
    for item in ETF_list:   
        df1 = pd.read_csv(dir + "list" + "_" + item + "_" + ".csv", encoding ="utf-8")
        print(item)
        df1.to_excel(writer, item)
# 执行写入Excel操作 -> 对于ETF_list，即申赎清单
print("ETF_lsit Done!!!")
print(".........")

with pd.ExcelWriter(dir + 'ETF_cons.xls', mode = "w+", decoding='utf-8') as writer:
    for item in ETF_list: 
        print(item)
        df2 = pd.read_csv(dir + "cons" + "_" + item + "_" + ".csv", encoding ="utf-8")
        df2.to_excel(writer, item)
# 执行写入Excel操作 -> 对于ETF_cons，即申赎成分
print("ETF_cons Done!")