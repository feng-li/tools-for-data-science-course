import pandas as pd

# 读取数据
df = pd.read_csv( gdp.csv , encoding= utf-8 )
(names, values, dates) = ([], [], [])
# 记得去除地区这个列名,遍历年份
for i in df.columns[1:]:
    for j, k in zip(df[i], df[ 地区 ]):
        # 输出地区、GDP值、年份数据
        print(k, j, i)
        names.append(k)
        values.append(int(j))
        dates.append(int(i.replace( 年 ,   )))
# 生成DateFrame格式的数据
data = {
     name : names,
     type :   ,
     value : values,
     date : dates
}
# 将数据转存为新的CSV文件
frame = pd.DataFrame(data)
# 设置编码格式,避免乱码
frame.to_csv( gdp_last.csv , encoding= utf_8_sig )
