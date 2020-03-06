import numpy as np
import pandas as pd
from pandas import read_csv
import locale
from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
locale.setlocale(locale.LC_CTYPE, 'chinese')    # 编码问题

debt = read_csv('debt.CSV', encoding='GBK')     # 读入
data = read_csv('600000.SH.CSV', encoding='GBK', header=-1)
market = read_csv('000001.csv', encoding='GBK')


def process_market():
    global market
    s = '2006-06-08'
    start_index = market[market['日期'] == s].index.values[0]
    s = '2016-06-08'
    end_index = market[market['日期'] == s].index.values[0]
    market = market.iloc[end_index:start_index + 1, [3]]  # 10年的上证指数收盘价，上证指数数据是倒序的
    market = market.sort_index(ascending=False)
    market = market.apply(pd.to_numeric, errors='coerce')   # 转化为数字
    market = np.log(market)  # log return rate
    market = market.diff()  # rm 股票收益率
    market = market.reset_index(drop=True)
    # rm 市场利率


def process_debt():
    global debt
    s = '2006年6月8日'
    start_index = debt[debt['日期'] == s].index.values[0]
    s = '2016年6月8日'
    end_index = debt[debt['日期'] == s].index.values[0]
    debt = debt.iloc[end_index:start_index+1, [1]]  # 10年的国债收盘价，国债数据是倒序的
    debt = debt.apply(pd.to_numeric, errors='coerce')   # 转化为数字
    debt = debt.sort_index(ascending=False)
    debt = debt.reset_index(drop=True)
    for i in range(debt.size):
        debt.iloc[i, 0] = debt.iloc[i, 0]/(100*253)     # 转成日收益率
    # rf 无风险利率


def process_stock():
    global data
    s = '2006-06-08'
    start_index = data[data.iloc[:, 2] == s].index.values[0]

    s = '2016-06-08'
    end_index = data[data.iloc[:, 2] == s].index.values[0]

    data = data.iloc[start_index:end_index + 1, [7]]  # 10年的股票收盘价

    data = data.apply(pd.to_numeric, errors='coerce')  # 转化为数字
    data = np.log(data)  # log return rate
    data = data.diff()  # ri 股票收益率
    data = data.reset_index(drop=True)


process_debt()      # rf
process_market()    # rm
process_stock()     # ri

debt = debt.iloc[0: data.size, :]       # size = 2436
data = data.iloc[1:, :]     # 第一个元素为NaN
debt = debt.iloc[1:, :]
market = market.iloc[1:, :]

data = np.array(data).flatten().T
debt = np.array(debt).flatten().T
market = np.array(market).flatten().T

Ri = data - debt
Rm = market - debt

plt.scatter(Rm, Ri)     # 绘图
plt.show()
# ri - rf = b(rm - rf) +e

df = pd.DataFrame({'x': Rm, 'y': Ri}, index=[i for i in range(data.size)])
model = ols('y~x', df).fit()
# 对回归模型进行检验
# Ri = a + bRm + e 验证a不显著不为0
print(model.summary())
