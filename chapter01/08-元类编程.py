# encoding: utf-8
"""
Created by Vic on 2018/6/19 20:19
取动态属性： 使用 @property 来装饰类里面的方法
设置动态属性： 使用 @动态属性名.setter 来装饰
__getattr__ 、__getattribute__
"""
import numbers
from datetime import datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


"""
使用实例.属性的方式获取属性值得时候，如果找不到该属性，就会调用 `__getattr__`（这个魔法函数可以加很多猥琐的操作）
使用实例.属性的方式获取属性值得时候，无条件就会调用 `__getattribute__` （这个函数能力更强，轻易不要动）
"""

"""
自定义属性描述符：一个类里面定义了 __get__、__set__、__delete__ 中的任意一个便是一个属性描述符
"""


class IntField:
    """数据描述符"""

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('需要传入整数类型')
        if value < 0:
            raise ValueError('年龄不能小于0')
        # 这里的赋值不能直接使用 instance.age = age 会导致无限地调用 __set__ 方法
        # 所以要将值放到 IntField 的实例上，取值的时候也从 IntField 的实例上取得
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    """非数据描述符（只实现 __get__ 方法）"""

    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


"""
如果 user 是某个类的实例，那么 user.age （以及等价的 getattr(user, 'age')）首先调用 __getattribute__。
如果类定义了 __getattr__ 方法，那么在 __getattribute__ 抛出 AttributeError 的时候就会调用到 __getattr__，
而对于描述符 __get__ 的调用，则是发生在 __getattribute__ 内部的。
user = User(), 那么 user.age 顺序如下：

(1) 如果 age 是出现在 User 或其基类的 __dict__ 中，且 age 是 data descriptor（数据描述符），那么调用其 __get__ 

(2) 如果 age 出现在 obj 的 __dict__ 中，那么直接返回 obj.__dict__['age']，否则

(3) 如果 age 出现在 User 或其基类的 __dict__ 中

(3-1) 如果 age 是 non-data descriptor，那么调用其 __get__ 方法，否则

(3-2) 返回 __dict__['age']

(4) 如果 User 有 __getattr__ 方法，调用 __getattr__ 方法，否则

(5) 抛出 AttributeError
"""


class User:
    def __new__(cls, *args, **kwargs):
        # 控制实例的生成过程，在实例生成之前（一定要返回类）
        return super().__new__(cls)

    def __init__(self):
        # 完善实例，在实例生成之后
        pass


"""
元类编程，元类其实就是创建类的类，即 type
通过元类，我们可以控制实例的创建过程
"""


class MetaClass(type):
    # 自定义的元类都要继承 type
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    pass
