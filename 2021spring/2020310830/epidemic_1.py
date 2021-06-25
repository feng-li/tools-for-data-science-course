#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.express as px
from datetime import datetime

init_notebook_mode()


# In[5]:


# 从 akshare 获 取 数 据
# df_all_history = ak.epidemic_history()

# 从 csv 文 件 获 取 数 据
df_all_history = pd.read_csv('epidemic_all_20200307.csv',index_col=0)
df_all_history


# In[6]:


df_all = df_all_history
# 将 字 符 串 格 式 的 日 期 另 保 存 为 一 列
df_all['dates'] = df_all_history['date']


# 将 字 符 串 格 式 的 日 期 转 换 为 日 期 格 式
df_all['date'] = pd.to_datetime(df_all['date'])


# In[21]:


# 国 外 ， 按 国 家 统 计
df_oversea = df_all.query("country!=' 中 国 '")
df_oversea.fillna(value="", inplace=True)
df_oversea


# In[17]:


# 用 plotly express 看下国外疫情分国家的整体走势

fig_oversea = px.line(df_oversea, x='dates', y='confirmed',
                      line_group='country',
                      color='country',
                      color_discrete_sequence=px.colors.qualitative.D3,
                      hover_name='country',
                     )

fig_oversea.show()


# In[22]:


# 现 有 数 据 演 示 从 2020 年 2 月 10 日 开 始
df_oversea_recent = df_oversea.set_index('date')
df_oversea_recent = df_oversea_recent['2020-02-10':]
df_oversea_recent


# In[23]:


# 由 于 部 分 国 家 ， 数 据 不 是 从 2020 年 2 月 10 日 开 始 的 ， 所 以 要 补 充 数 据 ， 数 值 为 0
# 数 据 在 excel 表 格 中 进 行 补 充 ， 这 里 进 行 读 取

df_oversea_buchong = pd.read_excel('epidemic_buchong.xlsx')
df_oversea_buchong['dates'] = df_oversea_buchong['date'].apply(lambda x:x.strftime('%Y-%m-%d'))
df_oversea_buchong.set_index('date', inplace=True)
df_oversea_buchong.fillna(value="", inplace=True)
print(df_oversea_buchong.info())
df_oversea_buchong


# In[24]:


# 合 并 补 充 数 据
df_oversea_recent_new = df_oversea_recent.append(df_oversea_buchong)
df_oversea_recent_new.sort_index(inplace=True)
df_oversea_recent_new


# In[29]:


# 用气泡图来对变化情况进行可视化
fig_oversea_recent = px.scatter(df_oversea_recent_new, x='dead', y='confirmed',
                                size='confirmed', text='country', color='country',
                                color_discrete_sequence=px.colors.qualitative.Light24,
                                animation_frame='dates',animation_group='country',
                                hover_name='country',
                                range_x=[-10,260],
                                range_y=[0,8000],
                                size_max=100,
                                template='plotly_white',
                               )
fig_oversea_recent.show()


# In[ ]:




