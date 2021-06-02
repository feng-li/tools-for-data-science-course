from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.cufe.edu.cn/index.htm")
bsObj=BeautifulSoup(html,"html.parser")
images=bsObj.findAll("img")
jpgs=bsObj.findAll("img",{"src":re.compile(".+\.jpg")})
for jpg in jpgs:
    print(jpg["src"])


        #采集所有【党政服务】的机构名称和URL链接地址，并显示
html=urlopen("http://www.cufe.edu.cn/zzjg/dzfw.htm")
bsObj=BeautifulSoup(html,"html.parser")
surr=bsObj.find("div",{"class":"dzfw"})
depts=surr.findAll("a")
for dept in depts:
    print(dept.get_text()+" "+dept["href"])
       #采集[服务指南]下面的所有栏目名称，并显示
surr2=bsObj.find("a",{"href":"../fwzn.htm"}).parent.parent
names=surr2.findAll("a")
for name in names:
    if name.get_text()=="服务指南":
        pass
    else:
         print(name.get_text())
        #尝试用 子标签（children）、 后代标签（descendants）、 兄弟标签（siblings）和父标签（parent）采集网页上的信息
me=bsObj.find("div",{"class":"nav"})
par=me.parent
bro=me.siblings
chil=me.children
des=me.descendants
print(par)
print(bro)
print(chil)
print(des)
       #采集3个及以上属性的a标签并显示     
aa=bsObj.findAll(lambda tag: len(tag.attrs)>=3)
for a in aa:
        print(a)

        #设计一个正则表达式，并采集相关数据
html=urlopen("http://dasai.lanqiao.cn/?lqnew=1")
bsObj=BeautifulSoup(html,"html.parser")
images=bsObj.findAll("img",{"src":re.compile(".+\.jpg")})
for image in images:
    print(image["src"])
        #设计一个lambda函数，并采集相关数据
tags=bsObj.findAll(lambda tag:len(tag.attrs)==3)
for tag in tags:
    print(tag)
