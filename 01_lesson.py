if __name__ == '__main__':
    print('6 is', type(6))
    print('1.6 is', type(1.6))
    # 变量分大小写的

    print(len("我是小妮"))
    print("小凌" in "我是小凌")
    print("小凌" in "我是小鹏")
    print("小凌" not in "我是小鹏")

    print("小飞在小张飞的那个位置", "小飞在小张飞的那个位置".find("小张飞"))
    print("小飞在小张飞的那个位置", "小飞在小张飞的那个位置".find("你下手"))
    # 找不到返回 -1

    # 字符的索引，就是指字符在字符串的位置，注意第一个是从0开始的
    tmp = "程序员小鹏"
    print("程序员小鹏检索为0的字符串为", tmp[0])

    # 字符串分隔，split函数
    # 以逗号为分割符，将程序员，小鹏分开
    print("程序员，小鹏".split(','))
    print("-"*30 + "End Section 3 String " + "-"*30)

    # 列表就是用[] 表示的一组有序数据， 每个数据之间用逗号隔开
    # 创建之后可以增加或者删除数据
    # 其中数据类型可以是不一样的
    # 新建一个空列表
    null_list = []
    print(null_list)
    num_list = [1,2,3]
    print(num_list)
    str_list = ["1", "2", "2", "3"]
    print(str_list)
    kinds_list = ["1", "2", 2.3]
    print(kinds_list)
    print(num_list * 2)
    print(num_list + kinds_list)
    # 往列表末尾插入4
    num_list.append(4)
    print("往列表末尾插入4", num_list)
    # 往列表第四位插入5
    num_list.insert(3, 5)
    print("往列表第四位插入5", num_list)
    # 获取列表中值出现的次数
    print("str_list 中字符2出现了", str_list.count('2'))
    # 获取值在列表的位置
    print("str_list 第一个2 出现在的位置", str_list.index("2"))
    # 获取指定位置的值
    print(str_list[1])
    # 获取一定范围的值，切片索引包括前面的，不包括后面的 （第一个到第二个的值为）
    print(kinds_list[0:2])

    # 删除列表中的值
    # pop根据位置删除，删除第三个
    print(num_list.pop(2))
    print(num_list)
    # remove按照值来删除 删除值为 1 的
    num_list.remove(1)
    print(num_list)

    # 对列表进行排序，默认是升序
    num_list.sort()
    print(num_list)

    print("-" * 30 + "End Section 4 列表 " + "-" * 30)

    # 字典
    # 字典是一种键值对的结构，类似于通过联系人姓名找到他的手机号码
    # 是以{key1:value1, key2:value2} 方式表示
    # 键（key）必须是唯一的， 但是 值（value） 可以重复
    # 新建一个空字典
    test_dict= {}

    # 往字典里插入新值
    test_dict["小飞"] = 18613234543
    test_dict["小爱"] = 13916190565
    print("新建了一个字典", test_dict)
    # 获取所有的keys
    print(test_dict.keys())
    # 获取所有的 values
    print(test_dict.values())
    # 获取字典里内一组组的键值对
    print(test_dict.items())

    # key 取 value
    print(test_dict["小飞"])

    student = {'小萌': '1001', '小智': '1002', '小强': '1003', '小明': '1004'}
    # value 取 key
    def get_key (dict, value):
        return [k for k, v in dict.items() if v == value]
    print(get_key (student, '1002'))

    print("-" * 30 + "End Section 5 字典 " + "-" * 30)

    # 元组
    # 元组和列表相似，但是还有两点不同
    # 1 元组的的元素不能改变，但是列表能改变
    # 2 元组是用小括号（）表示， 但是列表是[]

    # 新建一个元组
    tup = (1, 2, 3, 4, 5)
    print(tup)
    # 获取元组的长度
    print(len(tup))
    # 获取元组内的元素
    print("元组的的第三个元素是", tup[2])
    # 获取元组内一段范围的元素
    print("元组的第二到第三个元素是", tup[1:3])

    # 元组和列表的互换
    # 用list() 将元组转换为列表
    print(list(tup))
    # 用tuple()将列表转换为元组
    li = [1, 2, 3, 4, 5]
    print(tuple(li))






