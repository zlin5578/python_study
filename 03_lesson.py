import pandas as pd

print("-" * 30 + "Begin Section Series" + "-" * 30)
# Series 一维
# Series 是一种类似于 一维 数组的对象， 由一组数据和一组与之相关的索引组成
# 默认的索引从 0 开始
S1 = pd.Series(['a', 'b', 'c', 'd'])
print(S1)

# 传入索引
print("传入列表，自定义索引： ")
S2 = pd.Series(['a', 'b', 'c', 'd'], index=[1, 2, 3, 4])
print(S2)

# 传入字典， key为索引， value 为数据
print("传入字典： ")
S3 = pd.Series({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
print(S3)

# index 获得索引
print("index 获得索引： ")
print(S1.index)
print(S2.index)
print(S3.index)

# value 获得值
print(S1.values)
print("\n")


print("-" * 30 + "Begin Section DataFrame" + "-" * 30)
# DataFrame 二维
# DataFrame 是由一组数据与一堆索引（行索引 和 列索引）组成的表格形数据结构
# 默认的行索引和列索引都是从 0 开始
print("传入列表， 默认行索引和列索引")
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)

print("传入一个嵌套列表：")
df2 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']])
print(df2)

# 里面嵌套元组也可以

df2 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']],
                   columns=["小写", "大写"],
                   index=["一", "二", "三", "四"])
print(df2)

print("传入字典： ")
df3 = pd.DataFrame({"小写": ['a', 'b', 'c', 'd'], "大写": ['A', 'B', 'C', 'D']})
print(df3)

print(df3.columns)
print(df3.index)




