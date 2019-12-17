#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 下午3:59
# file : mine
"""
NOTICE:
1、暴力，得到所有三元组的和，然后找最小的
2、计算target与每个元素的差，然后就是计算两个数的和，与这些差尽可能的相近，然后再扩展，得到最后一个数的差，找到数组中与这个数最近的数
    复杂度没有降低
3、----排序双指针，两头开始，和比target大，则尾指针前移，比targget小，则头指针后移
"""
import numpy as np
def sum_3_closeset(list,target):
    list_sum_2_target = target-np.array(list)
    list_sum_1_target = list(map(lambda x:x-np.array(list),list_sum_2_target))
