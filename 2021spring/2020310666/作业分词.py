


python中结巴的分词切词功能




import jieba

txt = open("C:\\期末总结.txt","r",encoding='utf-8').read()
words = jieba.cut(txt)  ＃使用精确模式对文本进行分词
counts = {} ＃通过键值对的形式存储词语以及其出现的次数

for word in words:
  if len(word) == 1:           ＃单个词语不计算在内
    continue
    else:
      counts[word] = counts.get(word,0)
      
 items = list(counts.items())  ＃将键值对转换成列表
items.sort(key=lamba x: x[1], reverse=True)   ＃ 根据词语出现的次数进行由大到小的排列


for i in range(15):
  word, count = items[i]
  print("{0:＜5}{1:＞5}".format(word,count))
  
  
  
  
  具体举例说明结巴分词 
  
  
  
  
  
  
  encoding=utf-8
  
  import jieba
  seg_list = jieba.cut("我去了北京",cut_all=True)
  
  print "Full Mode:","/
  ".join(seg_list)＃全模式
  seg_list = jieba.cut("我去了北京",cut_all=false)
  
  print"Default Mode:"."/".join(seg_list) ＃默认模式
  
  输出
  Full Mode:我/去/去了/了/北/北京/京/
  Default Mode:我/去了/北京/
