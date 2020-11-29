import pandas as pd

print("-" *30 + "begin Section 导入数据" + "-" * 30)
df = pd.read_excel(r"/Users/yons/Desktop/py_help/04_lesson.xlsx")
print("excel 的数据是" + '*' * 30)
print(df, '\n')


df = pd.read_excel(r"/Users/yons/Desktop/py_help/04_lesson.xlsx")

# pandas.read_excel(
# io,  #string类型文件的路径或url.
# sheet_name=0,  #指定的excel中的具体某个或某些表的表名或表索引.
# header=0,  #以哪些行作为表头，也叫做列名.
# names=None, #自己定义一个表头(列名).
# index_col=None,  #将哪些列设为索引.
# usecols=None,  #指定读取excel中哪些列的数据,默认为None，表示读取全部.
# squeeze=False,  #默认为False,如果解析的数据只包含一列，则返回一个Series。
# dtype=None,  #接收dict,设置数据类型，具体到每列.
# engine=None,  #如果io不是缓冲区或路径，则必须将其设置为标识io。可接受的值是None、“xlrd”、“openpyxl”或“odf”.
# converters=None,  #类型为字典(dict).默认为None.进行值转换。{列名:str}
# true_values=None,  #默认:None,接收一个list，将在list中的值转换成True，只有在整列值都能转换成bool值时才能成功。
# false_values=None,  #默认:None,接收一个list，将在list中的值转换成False，只有在整列值都能转换成bool值时才能成功。
# skiprows=None,  #跳过excel中的某些行来读取数据.
# nrows=None,  #指定要读取excel表中哪些行的数据.
# na_values=None,  #设置指定值填充为NaN.
# keep_default_na=True,
# verbose=False, #布尔类型, 默认为 False.显示列表中除去数字列，NA值的数量.
# parse_dates=False,  #指定解析成日期格式的列.
# date_parser=None,  #funtion.指定解析日期格式的函数.
# thousands=None, #将字符串列解析为数字的数千个分隔符。
# comment=None, #将一个或多个字符传递给此参数以指示输入文件中的注释。
# skipfooter=0,  #省略指定行数的数据，从尾部数的行开始。
# convert_float=True, #布尔, 默认为 True.将积分浮点数转换为int（即1.0 - > 1）。
# mangle_dupe_cols=True,  #布尔类型，默认为True.重复列将被指定为“X”、“X.1”、“X.N”.
# **kwds)

df = pd.read_excel(r"/Users/yons/Desktop/py_help/04_lesson.xlsx",usecols=[0,3])
print(df, '\n')

df = pd.read_csv(r"/Users/yons/Desktop/py_help/04_lesson.csv",sep=',')
print(df, '\n')

df = pd.read_csv(r"/Users/yons/Desktop/py_help/04_lesson.csv",sep=',', nrows= 2)
print(df, '\n')

# 如果是 gbk 格式的csv ，在后面加 encoding = "gbk" 转化（通常中文转化为乱码的就是gbk了， utf-8 都是适配的）

# 导入txt文件
# read_table(), 是导入利用分隔符分开文件的通用函数
# 不仅可以导入 .txt 文件， 还可以导入.csv文件
df = pd.read_table(r"/Users/yons/Desktop/py_help/04_lesson.txt", encoding = "utf-16")
print(df, '\n')

print("-" *30 + "begin Section 熟悉数据" + "-" * 30)

# head() 默认显示前 5 行
print(df.head(3), '\n')

# shape 获取数据表的大小
print(df.shape, '\n')

# info() 获取数据类型
print(df.info(), '\n')

# describe() 获取数据分布 (一般为数据类型的)
print(df.describe(), '\n')
