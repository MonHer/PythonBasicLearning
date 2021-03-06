# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/11/14:59
# @Author : Yuye
# @File   : Homework_exam_3.py

"""
1. 实现⼀个函数，要求对⼀个列表⾥⾯所有数字求和，如果⾥ ⾯含有⾮数字的
元素。直接跳过。⽐如[1,2,3] 输出是5， 如果 是[1,2,4,”a”] 输出是7。 并在另外
⼀个包（⽬录）⾥⾯调⽤这个 函数
❖ 2. 已有字典dic={“name”:”xiaozhang ”,”sex”:”male”}, 访问字典 dic[“grade”]，
❖ 3. 实现⼀个不定长参数的函数def flexible(aa, *args, **kwargs):，
❖ 把传⼊的参数和值打印出来。⽐如传⼊参数是
❖ flexible(aa, 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
❖ 输出结果：(2, 3, 1, 2, 3)，{'a': 1, 'y': 5, 'b': 2, 'x': 4}
❖ ⾯试题：*args, **kwargs 有什么作⽤
"""

list1 = [1, 2, 3, 6, "a"]
for i in list1:
    if isinstance(i, int):
        pass
    else:
        list1.remove(i)

sum(list1)
print(sum(list1))

# 已有字典dic={“name”:”xiaozhang ”,”sex”:”male”}, 访问字典 dic[“grade”]，
"""
print key,dic[key],后面有个逗号，自动生成一个空格
print key + str(dic[key]),连接两个字符串，用的是加号，直接输出，中间不加逗号
"""
dic = {"name": "xiaozhang ", "sex": "male"}
print(type(dic))

for key in dic:
    print(key, dic[key])
    print(key + str(dic[key]))

for (k, v) in dic.items():
    print("dic[%s]=" % k, v)


# 实现⼀个不定长参数的函数def flexible(aa, *args, **kwargs)

def fiexible(aa, *args, **kwargs):
    """
    flexible(aa, 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
 输出结果：(2, 3, 1, 2, 3)，{'a': 1, 'y': 5, 'b': 2, 'x': 4}
    :param aa:
    :param args:
    :param kwargs:
    :return:
    """
    print(args)
    print(kwargs)
    return


fiexible("aa", 2, 3, x=4, y=5, *[1, 2, 3], **{'a': 1, 'b': 2})
