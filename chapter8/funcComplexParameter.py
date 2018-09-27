#! /usr/bin/python3

import pprint

# 演示使用**user_info来定义任意数量的键值对参数
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Tom', 'White',
                             location='princeton',
                             field='physics',
                             preference='spicy',
                             age=18,
                             working_experience=20)
# print(user_profile)
pprint.pprint(user_profile)