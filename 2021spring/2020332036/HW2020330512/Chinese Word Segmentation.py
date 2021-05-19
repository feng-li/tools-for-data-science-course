import jieba

seg_list = jieba.cut("生活就像海洋", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))

txt = open("To be dismembered.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

seg_list = jieba.cut(txt, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))

jieba.load_userdict("userdict.txt")
seg_list = jieba.cut(txt, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))
