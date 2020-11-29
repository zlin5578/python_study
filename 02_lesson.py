import pandas as pd
if __name__ == '__main__':
    print("lesson2")
    print("(常规运算符)10 / 20 = ", 10 / 20)
    print("（取商不包含余数）10 // 20 = ", 10 // 20)
    print("（取余数）10 % 20 = ", 10 % 20)
    print("返回x的y次幂 10 ** 20", 10 ** 20)

    # == != > < 逻辑判断
    # and or not  并 或 否

    print("-" * 30 + "循环语句" + "-" * 30)
    print("for循环")
    subjects = ["Excel", "SQL", "Python", "统计学"]
    for sub in subjects:
        print("小凌目前正在学习: {}".format(sub))

    S1 = pd.Series(['a', 'b', 'c', 'd'])
    print(S1)




