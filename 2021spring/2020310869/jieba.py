import jieba

text = "征战四海只为今日一胜，我不会再败了。"
# jieba.cut直接得到generator形式的分词结果
seg = jieba.cut(text)  
print(' '.join(seg)) 

# 也可以使用jieba.lcut得到list的分词结果
seg = jieba.lcut(text)
print(seg)
征战 四海 只 为 今日 一胜 ， 我 不会 再败 了 。
['征战', '四海', '只', '为', '今日', '一胜', '，', '我', '不会', '再败', '了', '。']
import jieba.analyse as analyse
text = "征战四海只为今日一胜，我不会再败了。"
# TF-IDF
tf_result = analyse.extract_tags(text, topK=5) # topK指定数量，默认20
print(tf_result)
# TextRank
tr_result = analyse.textrank(text, topK=5) # topK指定数量，默认20
print(tr_result)

['一胜', '再败', '征战', '四海', '今日']
['一胜', '再败', '征战', '四海', '今日']
jieba.lcut(sentence,cut_all=False,HMM=True) # 精确模式
jieba.lcut(sentence,cut_all=True,HMM=True) # 全模式
jieba.lcut_for_search (sentence, HMM=True) # 搜索引擎模式

sentence = "征战四海只为今日一胜，我不会再败了。"
#---------------result----------------
'今天天气 真 好' # 精确模式
'今天 今天天气 天天 天气 真好' # 全模式
'今天 天天 天气 今天天气 真 好' # 搜索引擎模式