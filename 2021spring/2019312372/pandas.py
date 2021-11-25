from pandas import Series,DataFrame
import pandas as pd
import string
alphas=string.ascii_letters  #alphas为字母字符串
zifu='。，、（）()'
data = {"Name":['LiHua','XiaoMin','XiaoHong'],"Age":[18,19,20],"Sex":["男","女","女"],"Grade":["大一","大二","大二"]}
f1=DataFrame(data,columns=['Name','Sex','Age','Grade'],index=['1','2','3'])
print(f1)
print()

s1 = ["Madam Curie was born in Poland in 1867 and she is a French physicist. When studying in Paris, she lived a poor life but worked very hard. She married with Pierre Curie in 1859 when they discovered polonium and radium. Thanks to this great discovery, she and her husband won the Nobel Prize. In 1911, Madam Curie won the Nobel Prize again after the death of her husband, making her become the only woman who had won two Nobel Prizes in the word. As a pioneer of successful woman, Madam Curie’s example had a remarkable influence on the whole world. Although she was famous, she cared little about money and fame and still went on with her scientific research."]
a=s1[0]
b=a.split()
for i in range(len(b)):  #去掉符号
    c=''
    for j in b[i]:
        if j  not in alphas :
            pass
        else:
            c=c+j
    b[i]=c
S1 = Series(b)
print(S1)
print()

s2=['一是进一步深化增值税改革。增值税通过延长抵扣链条对制造业产生减税效应,带动制造业升 级栜。按照增值税税率三档并两档方向,降低工业四基[关键基础材料、核心基础零部件(元器件)、先进 基础工艺、产业技术基础]增值税税率,对自主可控技术、国产产品减免增值税。']
a2=s2[0]
b2=[]
for i in range(len(a2)):
    if i !=' ':
        b2.append(a2[i])
for i in range(len(b2)):  #去掉符号
    if  b2[i] in zifu :
        pass
    else:
        c2=b2[i]
    b2[i]=c2
S2= Series(b2)
print(S2)
