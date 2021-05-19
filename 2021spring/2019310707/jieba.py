import jieba
import re
from collections import Counter
cut_words=""
for line in open('./text1.txt',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
print(all_words)
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

print('\n词频统计结果：')
for (k,v) in c.most_common(2):# 输出词频最高的前两个词
    print("%s:%d"%(k,v))
————————————————
版权声明：本文为CSDN博主「空字符（公众号：月来客栈）」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/the_lastest/article/details/81027387
