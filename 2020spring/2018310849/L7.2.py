#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
driver = webdriver.Chrome()


# In[2]:


driver.get("https://mail.qq.com/")


# In[12]:


driver.find_elements_by_xpath('//*[@id="switch_bottom"]').click()


# In[14]:


driver.find_elements_by_xpath('//*[@id="u"]).send_keys("********")


# In[ ]:


driver.find_elements_by_xpath('//*[@id="p"]).send_keys("********")


# In[15]:


driver.find_elements_by_xpath('//*[@id="loginform"]/div[4]/a').click()


# In[ ]:




