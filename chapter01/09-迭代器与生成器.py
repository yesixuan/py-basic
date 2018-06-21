# encoding: utf-8
"""
Created by Vic on 2018/6/21 07:09
Iterable 实现 __iter__
Iterator 继承 Iterable 必须实现 __next__
"""

# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性返回数据的方式
# 遍历的时候，调用的是 iter 内置方法，这个方法会寻找对象中的 __iter__（返回 Iterator），如果没有，就会退而求其次找 __getitem__
from collections import Iterator


class Company:
    # 可迭代对象
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


class MyIterator(Iterator):
    """
    迭代器
    自定义迭代器，继承迭代器（也可以不继承，那样就需要自己实现 __iter__ 方法）
    """

    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        try:
            word = self.iter_list[self.index]
        # 捕获的是 IndexError，抛出的是 StopIteration
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['tom', 'bob', 'jane'])
    my_itor = iter(company)
    # for 循环的本质
    while True:
        try:
            # next 内置方法会首先找 __iter__，不行就找 __getitem__
            next(my_itor)
        except StopIteration:
            pass
