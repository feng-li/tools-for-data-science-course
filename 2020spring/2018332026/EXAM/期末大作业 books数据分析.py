# -*- coding: gb2312 -*-
# ����˵��������4���ļ���
# �ļ�1��to_read.csv  ��ÿ���������ݣ��û�id�͸��û�������鼮id
# �ļ�2��books.csv���鼮�ĸ���id�����ƣ����ߵ���Ϣ
# �ļ�3��tags.csv��ÿ���������ݣ���ǩid�ͱ�ǩ����
# �ļ�4��book_tags.csv��ÿ���������ݣ�_goodreadsbook_id_ ����ǩid,��Ǵ�������to_read�е��鼮id�Ķ�Ӧ��ϵ������books.csv���ҵ���

# ����1���ҳ�����������50��������Ʋ����ɴ���ͼ
# ����2���ҳ���50�����Ӧ�����ŵ�10����ǩ������״ͼ����չʾ

import numpy as np
import pandas as pd
from pyecharts.charts import WordCloud  # �������ͼģ��
from pyecharts.charts import Bar  # ������״ͼģ��
from pyecharts.charts import Pie  # �����ͼģ��
from pyecharts import options as opts  # ����Ҫ������ģ��
from pyecharts.globals import ThemeType  # ����������ɫģ��

#  ----------  �ҳ�50������ͼ�� ---------
data = pd.read_csv('to_read.csv')
data_new = data.sort_values(by='book_id')  # ��book_id������ԭ����
# ��������book_id�н���ɸѡ(��ͬ���ಢͳ��)���������������ǰ50������
books_count = data['book_id'].value_counts().sort_values(ascending=False)
hostbooks_50_id = books_count[:50].index  # ����book_id��ǰ50���ݣ���Series����
hostbooks_50_count = books_count[:50].values
hostbooks_50 = pd.DataFrame({
    "book_id": hostbooks_50_id,
    "read_count": hostbooks_50_count
})
books = pd.read_csv('books.csv')
books_with_titles = books[['book_id', 'goodreads_book_id', 'title']]  # ȡ��ԭ������3������,2��[]
hostbooks_withtitles_50 = pd.merge(hostbooks_50, books_with_titles,  # �ϲ�2������
                                   on='book_id', how='left')  # ����book_id�У������Ϊ׼��50�У�
hostbooks_withtitles_50.to_csv("hostbooks50.csv", index=False)  # ����ΪCSV�ļ�������������
print("����ɸѡ��ϣ�����Ϊ hostbooks50.csv �ļ�")

#  ----------  �ҳ�10�����ű�ǩ ---------
tags = pd.read_csv('book_tags.csv')
# ��������tags���ݽ���ɸѡ��ѡ��'_goodreads_book_id_'����ǰ��hostbooks_withtitles_50��������ͬ��
hostbooks_tag = tags[tags['_goodreads_book_id_'].isin(hostbooks_withtitles_50['goodreads_book_id'])]
del hostbooks_tag['_goodreads_book_id_']  # ɾ������ʹ�õ���
hostbooks_tag_10 = hostbooks_tag.groupby('tag_id').sum()  # ����tag_id�н��з��鲢��������
hostbooks_tag_10 = hostbooks_tag_10.sort_values(by='count', ascending=False)[:10]  # ����ȡǰ10��

# ���´����ҳ�tag_id��Ӧ�ı�ǩ����
books = pd.read_csv('tags.csv')
hosttags_withtitles_10 = pd.merge(hostbooks_tag_10, books,  # �ϲ�2������
                                  on='tag_id', how='left')  # ����tag_id�У������Ϊ׼��10�У�
hosttags_withtitles_10.to_csv("hostbooks_tag10.csv", index=False)  # ����ΪCSV�ļ�������������
print("����ɸѡ��ϣ�����Ϊ hostbooks_tag10.csv �ļ�")

# ����50������ͼ�����ͼ
hostbooks = pd.read_csv('hostbooks50.csv')
wordcloud = WordCloud()
words = [list(z) for z in zip(hostbooks.title.tolist(), hostbooks.read_count.tolist())]
wordcloud.add('����ͼ���', words, word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='50��������ϲ����ͼ��'))
wordcloud.render('hostbooks.html')

# ������������10��ͼ����״չʾͼ
hostest_10_books = pd.read_csv('hostbooks50.csv')[:10]  # ȡ������10����
bar = Bar(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,  # ��������ɫ�ͳߴ�
    width='640px',
    height='480px'))
bar.set_global_opts(title_opts=opts.TitleOpts(
    title='�����ŵ�10����'),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20)))  # ���ñ�����ת�Ƕ�

bar.add_xaxis(hostest_10_books['title'].tolist())  # ��������ת��Ϊ�б��ʽ�������޷���ͼ
bar.add_yaxis('�����鼮�����Ƽ���', hostest_10_books['read_count'].tolist())

bar.render('����ͼ��.html')  # ��Ⱦbarͼ������html�ļ�

# ����10�������ű�ǩ�ı�ͼ
hostest_tags = pd.read_csv('hostbooks_tag10.csv')[1:10]
pie = Pie()
datas = [list(z) for z in zip(hostest_tags['tag_name'], hostest_tags['count'])]
pie.add("��ǩ�ȶ�", datas,
        radius=['20%', '80%'],  # Բ����ͼ���⻷�뾶���б�����
        rosetype='area')  # ����õ����Բ����ͼ
pie.set_global_opts(title_opts=opts.TitleOpts(title=''))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

pie.render('���ű�ǩ.html')  # ��Ⱦpieͼ������html�ļ�
