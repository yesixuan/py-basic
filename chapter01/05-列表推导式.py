# encoding: utf-8
"""
Created by Vic on 2018/6/4 22:37
"""

# 过滤操作
odd_list = [i for i in range(21) if 1 % 2 == 1]


# 逻辑复杂的情况（map 与 filter 结合）
def handle_item(item):
    return item * item


odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]

print(odd_list)

# 这样是得到一个生成器，可以通过 list() 转成一个 list
odd_list = (i for i in range(21) if 1 % 2 == 1)

# 字典推导式（键值对互换）
my_dict = {
    'vic': 22,
    'bobby': 23,
    'moo': 5
}
reversed_dict = {
    value: key for key,
    value in my_dict.items()
}
