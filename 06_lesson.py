print("-" * 30 + " Begin Section 6 开场" + "-" * 30)
print("这是Python的第六次课程，主要讲数据的预处理")
print("1. 数据类型转换 \n2. 索引设置")
print("-" * 30 + "End Section 0 开场" + "-" * 30)
print("\n")

import pandas as pd
# Section 1 数据类型转换
df = pd.read_excel(r"/Users/yons/Desktop/py_help/04_lesson.xlsx", sheet_name="Sheet3")
df1 = df

# python 里面有六种主要的类型， int, float, object, string, unicode, datetime64[ns]
# 我们现在主要掌握四种 int, float, string, datetimes
# 查看某一列的数据类型, dtype
print(df["观看次数"].dtype, '\n')
print(df["发布时间"].dtype, '\n')

# 转换某一列的数据类型, astype()
# 将观看次数列的数据类型转换为float
print(df["观看次数"].astype("float64"))
print('\n')

# Section 2 索引设置
# 索引就是行标和列标
# 用columns， index 来设置
print(df, '\n')
df.index = [1,2,3,4,5]
print("给表格添加行索引：")
print(df, '\n')

# 用set_index() ,指明要用做行索引的列的名称
print("指明 观看次数 列当作行索引： ")
# 不会改变原先的表格， 所以要赋值
df = df.set_index("观看次数")
print(df, '\n')

df = df1
# 重命名列索引
df = df.rename(columns={"发布时间": "新发布时间"})
print(df, '\n')

# 改名行索引
df = df1
df = df.rename(index ={1:"一", 2:"二", 3:"三", 4:"四",5:"五"})
print(df, '\n')



