# encoding: utf-8
"""
Created by Vic on 2018/6/6 07:36
wtforms 是如何实现数据校验的，答案就在这里
"""

import numbers


class InField:
    """
    实现了以下三个魔法函数之一的类就叫做属性描述符
    """

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value

    def __delete__(self, instance):
        pass


class User:
    age = InField()


if __name__ == '__main__':
    user = User()
    user.age = '30'  # 传入字符串的话，会抛出异常
    print(user.age)
