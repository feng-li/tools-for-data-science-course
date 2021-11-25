

split = article.split()
print(split)

#使用空格替换标点符号
article = article.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","")





#大写字母转换成小写字母
exchange = article.lower();
print(exchange)



#生成单词列表
list = exchange.split()
print(list)




#生成词频统计
dic = {}
for i in list:
    count = list.count(i)
    dic[i] = count
print(dic)



#排序
dic1= sorted(dic.items(),key=lambda d:d[1],reverse= True)
print(dic1)




#输出词频最大的前十位单词
for i in range(10):
    print(dic1[i])
