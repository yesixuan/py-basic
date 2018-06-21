# encoding: utf-8
"""
Created by Vic on 2018/6/4 07:35
"""
import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        """切片的关键"""
        cls = type(self)
        # 切片时得到的参数是 slice 对象
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['a', 'b', 'c', 'd', 'e']
group = Group(company_name='imooc', group_name='user', staffs=staffs)
sub_group = group[:2]
print(sub_group)
