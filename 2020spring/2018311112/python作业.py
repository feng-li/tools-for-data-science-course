# In[1]:


a = [1,2,3]
a


# In[2]:


type(a)


# In[3]:


a[0]




# In[4]:


a.append(4)
a


# In[5]:


a.insert(2,'a')
a


# In[6]:


a.remove('a')  
a


# In[7]:


del a[3]  
a


# In[8]:


b = [4,5,6]
a.extend(b)  
a


# In[9]:


a.pop(2)  


# In[10]:


a.reverse()  
a


# In[11]:


a.sort()  
a


# In[12]:


a.count(3)  


# In[13]:


a.index(2)  


# In[14]:


a.pop()  


# In[15]:


c1 = a
c2 = a[:]
c3 = a.copy()
c1,c2,c3


# In[16]:


a.append(6)
[c1,c2,c3] 




# In[17]:


m = [[1, 2, 3, 4],[5, 6, 7, 8, 9],[ 10, 11, 12]]
type(m)


# In[18]:


print(m)


# In[19]:


m[1][2]



# In[20]:


list(range(1,10,2))

# In[21]:


[x for x in range(1, 11)]


# In[22]:


[m + n for m in 'ABC' for n in 'XYZ']


# ### 集合

# In[23]:


a = {1,2,2,'a','a','bc'}  
a


# In[24]:


type(a)


# In[25]:


'a' in a  

# In[26]:


b = {1,3,'b','c'}
a | b


# In[27]:


a & b  


# In[28]:


a - b  


# In[29]:


a ^ b   


# In[30]:


set('122abb')



# In[31]:


a = 1,'a','b'   
a


# In[32]:


type(a)


# In[33]:


b = [1,'stacey']
c = a,b  
c


# In[34]:


c[0]


# In[35]:


c[0][1]


# In[36]:


c[0] = 1


# In[37]:


c[1][1]=2
c




# In[38]:


tel = {'Stacey':520, 'Mary':462, 'Joey':639}
print(tel)
type(tel)


# In[39]:


tel = dict(Stacey= 520, Mary = 462, Joey = 639)
tel


# In[40]:


tel = dict([('Stacey',520),('Mary',462),('Joey',639)])
tel


# In[41]:


print(tel.keys())
print(tel.values())  


# In[42]:


list(tel.keys())


# In[43]:


sorted(tel.keys())  


# In[44]:


tel['Stacey']


# In[45]:


'Mike' in tel


# In[46]:


tel['Honey'] = 880  
tel


# In[47]:


tel['Honey'] = 890  
tel


# In[48]:


del tel['Joey']  
tel




# In[49]:


import math
dir(math)


# ##### way1

# In[50]:


import math
math.exp(1)


# ##### way2

# In[51]:


import math as mt
mt.exp(1)


# ##### way3

# In[52]:


from math import exp 
exp(1) 


# ##### way4

# In[53]:


from math import exp as myexp 
myexp(1)


# #### numpy

# In[54]:


import numpy as np
A = np.array([[1,2],[3,4]])
A


# ##### 求矩阵转置

# In[55]:


A.T


# #### scipy

# In[56]:


from scipy import linalg
B = linalg.inv(A) # 求矩阵的逆
B


# ##### 矩阵乘法

# In[57]:


A.dot(B) 


# #### matplotlib(2D绘图库）

# In[58]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,4,6,2,4,8]

plt.plot(x, y)


# ### 函数

# #### 汉诺塔

# In[59]:


def move(n, a, b, c):
    if n == 1:
            print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


# In[60]:


move(3, 'A', 'B', 'C')


# ### 生成器

# In[61]:


def triangles(n):   
    L = [1]
    for x in range(n):
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


# In[62]:


for x in triangles(10):   
    print(x)


# ### 高阶函数

# In[63]:


def minus(x, y, f):
    return f(x) - f(y)


# In[64]:


minus(1, 0, exp)


# In[65]:


list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) 

# In[66]:


def normalize(name):  
    name = name.lower()
    name = name.capitalize()
    return name


# In[67]:


L = ['StaceY', 'LISA', 'joey']
list(map(normalize, L))


# In[68]:


list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15]))  

# In[69]:


sorted([30, 5, -12, 9, -21], key=abs) 



