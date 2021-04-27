# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:39:22 2021
@author: 皇后
展示股票K线图
"""
# 导包
from matplotlib.pylab import date2num
import matplotlib.pyplot as plt #注意导包的时候要导入pyplot
#import scipy as sp
import pandas as pd
#import csv
import datetime as dt
#获取股票信息的包。运行的时候发现这个包不在Anaconda里面所以又学习了怎么自己安装包
import tushare as ts
# #df = ts.get_hist_data('600519',start='2019-01-01',end='2019-12-31')
ts.set_token('fb1fa5ad798f5326404eb8a8887fae4fc2f11e1b0839975bc9ce558a')
pro=ts.pro_api()
import mplfinance as mpf #画K线图的包，也要自己下

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#日期转换
def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = dt.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_date

class Stock:
    def __init__(self, stknum):
        self.stknum=stknum
    
    #提示用户传入股票代码的信息
    def get_num(self):
        stknum=input("Please enter the Stock Number you want to check(ending with .SH or .SZ):")
        self.stknum=stknum
    
    #判断股票所处市场
    def which_ex(self):
        ex=int(self.stknum) #整除，得到前三位数
        # print(ex)
        # print(ex//1000)
        if ex//1000==000 or ex//1000==200:
            #print('A')
            return '.SZ' #深交所
        elif ex//10000==60 or ex//1000==900:
            #print('B')
            return'.SH'  #上交所
        else:
            #print('C')
            return ''
    
    #收集该股票对应交易所指数收益率
    def get_ex(self):
        pass
        
    #收集该股票的信息
    def plot_stk(self,istrading:bool=False,tight:bool=False,**kwargs):#关键字参数，默认值参数，参数注释
        if 'start_date' in kwargs:
            self.start_date=kwargs['start_date']
        else:
            self.start_date='2021-01-01'
        if 'end_date' in kwargs:
            self.end_date=kwargs['end_date']
        else:
            self.end_date='' #没设置就置空
        
        '''
        df=ts.get_hist_data(str(stknum),start='2019-3-1',end='2020-3-1'start=str(start_date),str(end=end_date))
        新的pro端口不再有get_hist_data()函数,改为daily()
        fields='ts_code,trade_date,close,volume_ratio,pe,pb'
        df=ts.daily_basic(ts_code=stknum,trade_date='20190301',fields=fields)
        mystock=df.iloc[::-1] #将结果转置，存储为一个数据框mystock
        temp_start_date=end_date-dt.timedelta(days=-365)#时间过去一年
        start_date=temp_start_date.isoformat()
        '''
        #设置时间
        if not self.end_date:
            self.end_date=dt.datetime.today().strftime('%Y-%m-%d')

        #读取近一年的股票信息
        df=ts.get_k_data(self.stknum,self.start_date,self.end_date)
        
        #如果没找到这个股票的信息
        if df.empty:
            print('\nStock Information not found.\nPlease check or try anthor options.')
            return False
        
        #获取股票名称
        data=pro.stock_basic(ts_code=self.stknum+self.which_ex())
        self.name=data.loc[0,'name']
        #将字符串转化为日期型数据
        df['date']=pd.to_datetime(df['date'])
        df.set_index('date',inplace = True)
        '''
        df_arr=df.values#将DataFrame中的数据转化为二维数组，用df接收
        df_arr[:,0]=date_to_num(df_arr[:,0]) #将二维数组中的日期转化为数值型格式
        绘制K线图
        (fig,ax)=plt.subplots(figsize=(12,5))#设置画布大小
        mpf.candlestick2_ochl(ax,df['open'],df['close'],df['high'],df['low'],width=0.6,
                              colorup='r',colordown='g')#设置图形情况，已过期
        ohlc = list(zip(np.arange(0,len(df.index)),
                        dt['open'],dt['close'],dt['high'],dt['low']))#使用zip方法生成数据列表 
        '''
        # 调用make_marketcolors函数，定义K线颜色
        mc = mpf.make_marketcolors(
            up='red',       # 上涨K线的颜色
            down='green',   # 下跌K线的颜色
            edge='',        # 蜡烛图箱体的颜色，这里选择不要边界颜色
            volume='grey',  # 成交量柱子的颜色
            wick='black',   # 蜡烛图影线的颜色
        )
        
        # 调用make_mpf_style函数，自定义图表样式
        # 函数返回一个字典，查看字典包含的数据，按照需求和规范调整参数
        mystyle = mpf.make_mpf_style(base_mpl_style='ggplot',
                                     marketcolors=mc,
                                     rc={'font.family': 'SimHei'})
        
        #绘制K线走势
        mpf.plot(df,
                 type='candle',
                 title='%s\n%s至%s'%(self.name,self.start_date,self.end_date),
                 ylabel='价格(人民币)',
                 style=mystyle,             #自定义格式
                 volume=True,               #显示成交量
                 ylabel_lower='成交量(股)',  #纵轴标签
                 figratio=(12, 6),          #设置图标大小
                 mav=(5,10,20),             #添加均线
                 tight_layout=tight,        #使用紧凑型的布局方式
                 xrotation=0,               #设置x轴标签的旋转角度
                 show_nontrading=istrading,#显示非交易日
                 datetime_format='%Y-%m-%d',#设置横轴日期格式
                 #savefig='%sK线图'%(self.name) + '.jpg'
                 )        
        '''        
        data: pd.DataFrame, 包含’Open’,‘High’,‘Low’,‘Close’字段，如果要显示成交量，还要提供’Volume’，默认时间序列索引(DatetimeIndex)
        type: 图表类型，可选值包含：‘ohlc’, ‘candle’, ‘line’, ‘renko’, ‘pnf’
        title: 标题
        ylabel: 纵轴标签
        style: 蜡烛图样式，mplfinance提供了很多内置样式
        volume: True表示添加成交量，默认False
        ylabel_lower: 成交量的Y轴标签
        show_nontrading: True显示非交易日，默认False
        figratio: 控制图表大小的元组
        mav: 整数或包含整数的元组，是否在图表中添加移动平均线
        '''

if __name__ == '__main__':
    s=Stock('600519')
    s.plot_stk(start_date='2021-01-01',tight=False)
