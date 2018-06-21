# encoding: utf-8
"""
Created by Vic on 2018/5/31 08:12
抽象基类类似于 Java 中的'接口'概念，用于强制使用者来实现某些方法
自己实现抽象基类的思路：定义一个基类，在需要子类重写的方法内部抛出异常。如此这般，子类若没有重写该方法时，就调用该方法就会报错
还有一种方法就是借助 abc 模块
"""

import abc


class CacheBase(metaclass=abc.ABCMeta):
    def __init__(self, arr):
        self.arr = arr

    @abc.abstractmethod
    def getter(self):
        pass

    @abc.abstractmethod
    def setter(self, newArr):
        pass


class RedisCache(CacheBase):
    """
    继承抽象基类的类必须要实现抽象基类中 @abc.abstractmethod 装饰器修饰的抽象方法
    """
    def getter(self):
        return self.arr

    def setter(self, newArr):
        self.arr = newArr


redis_cache = RedisCache(['1', '2', '3'])
