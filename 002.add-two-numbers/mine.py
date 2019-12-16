#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/16 下午2:53
# file : mine
"""
NOTICE:
用list的形式实现高位加和
需要循环
高位依赖低位的值
并且保证list的长度要相同

复习，python的列表？
"""
import exceptions
import numpy as np
def sum_linked_list(list1,list2):
    if len(list1)<>len(list2):
        exceptions.ValueError("lengths dont match!")
    exp_list = np.zeros(len(list1))
    result = np.zeros(len(list1))
    for index in range(len(list1)):
        if index==0:
            tmp_result = list1[index]+list2[index]
        elif index<len(list1):
            tmp_result = list1[index] + list2[index] + exp_list[index-1]
        exp_list[index] = tmp_result/10
        result[index] = tmp_result%10
    print result
    print exp_list
    if exp_list[-1]>0:
        print 'exp_list[-1]>0'
        result = np.append(result,exp_list[-1])# np的运算都有新的对象，不是在址运算
    return list(result)

if __name__=='__main__':
    list1 = [2,4,5]
    list2 = [5,6,4]
    print sum_linked_list(list1,list2)






