import jieba
 
seg_list = jieba.cut("美丽的安徽黄山迎客松",cut_all=True)
print("Full Mode:", "/ ".join(seg_list)  )    #全模式
 
seg_list = jieba.cut("美丽的安徽黄山迎客松",cut_all=False)
print("Default Mode:", "/ ".join(seg_list)  ) #精确模式
 
seg_list = jieba.cut("这里是美丽的安徽黄山迎客松")    #默认是精确模式
print(", ".join(seg_list)  )
 
seg_list = jieba.cut_for_search("这里是美丽的安徽黄山迎客松，祖国的大好河山！") #搜索引擎模式
print(", ".join(seg_list) 
