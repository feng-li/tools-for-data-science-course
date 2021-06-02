import re
import pandas as pd

#因为我暂时还不会在github上显示打开文件，所以这里的文件路径就不写了

path = '...'

f = open(path, "r")
passage = f.read()

char_list = jieba.cut(passage, cut_all=0)
char_set = set(char_list)
dict = {}
dict.fromkeys(char_set, 0)
for i in char_list:
  if len(i) >= 2:
    dict[i] += 1
  if len(i) < 1:
    try:
      del dict[i]

word_count = pd.DataFrame(dict)
# 这里word_count就是 关于词频统计的 DataFrame数据结构
    


  
