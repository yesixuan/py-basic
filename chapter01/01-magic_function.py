# encoding: utf-8
"""
Created by Vic on 2018/5/30 06:56
魔法函数
"""


class Company(object):
    """
    __getitem__ 将一个对象变成可遍历对象
    这个对象同样可以进行切片操作
    """

    def __init__(self, employee_list):
        self.emplayee = employee_list

    def __getitem__(self, item):
        return self.emplayee[item]

    def __len__(self):
        return len(self.emplayee)

    def __str__(self):
        """在解释器中会调用这个函数输出到命令行"""
        return ','.join(self.emplayee)

    def __repr__(self):
        """在调用 print 函数打印该对象时， 会调用该方法"""
        return ','.join(self.emplayee)


company = Company(['a', 'b', 'c'])
print(company)

for em in company:
    print(em)
