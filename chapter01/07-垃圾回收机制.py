# encoding: utf-8
"""
Created by Vic on 2018/6/19 09:06
基础类型与引用类型
垃圾回收使用标记计数方法（一个值每被赋给一个新的变量就会加一）
在函数中使用参数默认值的时候，如果这个默认值时引用类型，并且在调用该方法时，没有传这个参数，就会有坑
"""

class Company:
    # 这里的默认 staffs 就会有隐患
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
