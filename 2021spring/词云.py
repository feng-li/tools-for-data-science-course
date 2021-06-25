import jieba,numpy
from PIL import Image#导入PIL模块处理图片
from wordcloud import WordCloud #导入词云模块
words = open('ylxb.txt',encoding='utf-8').read()#打开文件，获取
new_words = ' '.join(jieba.cut(words))#分词
alice_mask = numpy.array(Image.open('gaogenxie.jpg'))
#使用pil模块打开这个图片，然后用numpy获取到这个图片的属性
wordcloud = WordCloud(width=1000, #宽度
                      height=860,  #高度
                      margin=2, #边距
                      mask=alice_mask,
                      background_color='#d4ff80',#指定背景颜色，颜色代码
                      font_path='C:\Windows\Fonts\Sitka Banner\msyh.ttc'#指定字体文件
                      )
wordcloud.generate(new_words) #分词
wordcloud.to_file('ylxb3.jpg')#保存到图片
