#分词及词频统计
import jieba
import jieba.posseg as peg
stopWords = [line.strip() for line in open('stopwords.txt', encoding='utf-8').readlines()]
txt = open("azhong.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if word not in stopWords:
        if len(word)==1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(50):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


#出于美观考虑，词云图用R语言绘制
#调用词云图包
library (wordcloud2)
#画 词 云 图
wordsf <- read_excel(”C:/ Users/7799701/Desktop/aaa/wordsf . xlsx”)
wordcloud2(wordsf , color = 'random- light ' ,minSize = 3, gridSize = 2,shape=” circle ”)


#情感分析代码简单版
#由于期末时间紧张，故粗浅的写了一段基于情感词典分析文本情感倾向的代码，局限性明显，还请老师见谅
import jieba
#积极词典
f=open(”C:/ Users/7799701/Desktop/词 典/正 面 情 感 词 语 （中 文） . txt” , 'r ')
ku1=[]

for line in f . readlines () :
    line=line . strip ( ' \n ')
    ku1.append( line )
'''
#消极词典
b=open(”C:/ Users/7799701/Desktop/词 典/负 面 情 感 词 语 （中 文） . txt ” , ' r ')
ku2=[]
for line in b. readlines () :
    line=line . strip ( ' \n ')
    ku2.append( line )
'''

#正向程度词典
c=open(”C:/ Users/7799701/Desktop/词 典/程 度 正 向 词 语 （中 文） . txt” , 'r ')
ku3=[]
for line in c . readlines () :
    line=line . strip ( '\n ')
    ku3.append( line )

#负向程度词典
d=open(”C:/ Users/7799701/Desktop/词 典/程 度 负 向 词 语 （中 文） . txt” , 'r ')
ku4=[]
for line in d. readlines () :
    line=line . strip ( '\n ')
    ku4.append( line )

#待分析（积极）
a=open(”C:/ Users/7799701/Desktop/data . txt” , 'r ' ,encoding=”utf -8”)
with open(”C:/ Users/7799701/Desktop/result . txt” ,”w”) as g:
#单个句子分词
    for line in a. readlines () :
        line=list ( jieba . cut( line ))

#初始化分数
score=0

    for k in range(0 , len ( line )) :
        line [k ] . strip ()
        line [k -1]. strip ()
        if line [k] in ku1:
            score=score+1

        if k==0:
            score=score
        elif line [k-1] in ku3:
            score=score+0.5
        elif line [k-1] in ku4:
            score=score -0.5
        else :
            score=score

        g. write ( str ( score )+”\n”)
#待分析（消极）
'''
for k in range(0 , len ( line )) :
    line [k ] . strip ()
    line [k -1]. strip ()
if line [k] in ku2:
    score=score -1

    if k==0:
    score=score
    elif line [k-1] in ku3:
        score=score -0.5
    elif line [k-1] in ku4:
        score=score+0.5
    else :
        score=score

    g. write ( str ( score )+”\n”)
'''
