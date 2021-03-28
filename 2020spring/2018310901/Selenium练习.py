#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
driver = webdriver.Firefox()


# In[ ]:


driver.get("https://www.bing.com/")


# In[ ]:


driver.find_element_by_id("sb_form_go").click()


# In[ ]:


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("Firefox Headless Browser Invoked")


# In[ ]:


driver.get("https://www.baidu.com/")


# In[ ]:


for result in results:
    print(result.text)


# In[ ]:


driver.close()

