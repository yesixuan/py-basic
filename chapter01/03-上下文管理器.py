# encoding: utf-8
"""
Created by Vic on 2018/6/3 15:09
上下文管理器，在真正代码执行的前后可以加上一段固定的逻辑，使代码更优雅
"""


class Sample:
    """
    通过魔法函数来实现上下文管理器
    """

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do_something(self):
        print('doing something')


with Sample() as sample:
    print(type(sample))

import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    yield {}
    print('file end')


with file_open('xx.txt') as f_opened:
    print('file processing')
