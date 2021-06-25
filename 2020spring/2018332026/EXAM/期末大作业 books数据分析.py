# -*- coding: gb2312 -*-
# 代码说明：共有4个文件：
# 文件1：to_read.csv  ，每行两个数据，用户id和该用户想读的书籍id
# 文件2：books.csv，书籍的各类id，名称，作者等信息
# 文件3：tags.csv，每行两个数据，标签id和标签名称
# 文件4：book_tags.csv，每行三个数据：_goodreadsbook_id_ ，标签id,标记次数（和to_read中的书籍id的对应关系可以在books.csv里找到）

# 功能1：找出最多人想读的50本书的名称并做成词云图
# 功能2：找出这50本书对应最热门的10个标签并用柱状图进行展示

import numpy as np
import pandas as pd
from pyecharts.charts import WordCloud  # 导入词云图模块
from pyecharts.charts import Bar  # 导入柱状图模块
from pyecharts.charts import Pie  # 导入饼图模块
from pyecharts import options as opts  # 导入要素配置模块
from pyecharts.globals import ThemeType  # 导入主题颜色模块

#  ----------  找出50本热门图书 ---------
data = pd.read_csv('to_read.csv')
data_new = data.sort_values(by='book_id')  # 按book_id列排序原数据
# 以下语句对book_id列进行筛选(相同归类并统计)并按降序排序并输出前50的数据
books_count = data['book_id'].value_counts().sort_values(ascending=False)
hostbooks_50_id = books_count[:50].index  # 返回book_id的前50数据，是Series数据
hostbooks_50_count = books_count[:50].values
hostbooks_50 = pd.DataFrame({
    "book_id": hostbooks_50_id,
    "read_count": hostbooks_50_count
})
books = pd.read_csv('books.csv')
books_with_titles = books[['book_id', 'goodreads_book_id', 'title']]  # 取出原数组中3列数据,2层[]
hostbooks_withtitles_50 = pd.merge(hostbooks_50, books_with_titles,  # 合并2个数组
                                   on='book_id', how='left')  # 依据book_id列，以左边为准（50行）
hostbooks_withtitles_50.to_csv("hostbooks50.csv", index=False)  # 保存为CSV文件，不含索引列
print("数据筛选完毕，保存为 hostbooks50.csv 文件")

#  ----------  找出10个热门标签 ---------
tags = pd.read_csv('book_tags.csv')
# 以下语句对tags数据进行筛选，选出'_goodreads_book_id_'列在前面hostbooks_withtitles_50数组中相同列
hostbooks_tag = tags[tags['_goodreads_book_id_'].isin(hostbooks_withtitles_50['goodreads_book_id'])]
del hostbooks_tag['_goodreads_book_id_']  # 删除不再使用的列
hostbooks_tag_10 = hostbooks_tag.groupby('tag_id').sum()  # 按照tag_id列进行分组并汇总数据
hostbooks_tag_10 = hostbooks_tag_10.sort_values(by='count', ascending=False)[:10]  # 排序并取前10个

# 以下代码找出tag_id对应的标签内容
books = pd.read_csv('tags.csv')
hosttags_withtitles_10 = pd.merge(hostbooks_tag_10, books,  # 合并2个数组
                                  on='tag_id', how='left')  # 依据tag_id列，以左边为准（10行）
hosttags_withtitles_10.to_csv("hostbooks_tag10.csv", index=False)  # 保存为CSV文件，不含索引列
print("数据筛选完毕，保存为 hostbooks_tag10.csv 文件")

# 制作50本热门图书词云图
hostbooks = pd.read_csv('hostbooks50.csv')
wordcloud = WordCloud()
words = [list(z) for z in zip(hostbooks.title.tolist(), hostbooks.read_count.tolist())]
wordcloud.add('热门图书榜', words, word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='50本读者最喜欢的图书'))
wordcloud.render('hostbooks.html')

# 制作其中最热10本图书柱状展示图
hostest_10_books = pd.read_csv('hostbooks50.csv')[:10]  # 取出最热10本书
bar = Bar(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,  # 配置主题色和尺寸
    width='640px',
    height='480px'))
bar.set_global_opts(title_opts=opts.TitleOpts(
    title='最热门的10本书'),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20)))  # 设置标题旋转角度

bar.add_xaxis(hostest_10_books['title'].tolist())  # 把数据列转换为列表格式，否则无法作图
bar.add_yaxis('热门书籍读者推荐榜', hostest_10_books['read_count'].tolist())

bar.render('热门图书.html')  # 渲染bar图，生成html文件

# 制作10个最热门标签的饼图
hostest_tags = pd.read_csv('hostbooks_tag10.csv')[1:10]
pie = Pie()
datas = [list(z) for z in zip(hostest_tags['tag_name'], hostest_tags['count'])]
pie.add("标签热度", datas,
        radius=['20%', '80%'],  # 圆环饼图内外环半径，列表类型
        rosetype='area')  # 设置玫瑰型圆环饼图
pie.set_global_opts(title_opts=opts.TitleOpts(title=''))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

pie.render('热门标签.html')  # 渲染pie图，生成html文件
