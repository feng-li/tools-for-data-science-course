#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests_html import HTMLSession
session=HTMLSession()
url='https://blogs.worldbank.org/zh-hans/opendata/2021nianshijiefazhanbaogaoshujugaishanshenghuo'
r=session.get(url)
print(r.html.text)


# In[ ]:




